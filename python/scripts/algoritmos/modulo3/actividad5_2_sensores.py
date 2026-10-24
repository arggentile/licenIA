import random
import threading
from abc import ABC, abstractmethod
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass
from datetime import datetime


# ---------------------------------------------------------------------------
# Lectura: dato inmutable (frozen) para que nadie pueda alterarla una vez creada
# ---------------------------------------------------------------------------
@dataclass(frozen=True)
class Lectura:
    valor: float
    momento: datetime
    anormal: bool


class LecturaInvalidaError(ValueError):
    """Se lanza cuando un valor está fuera del rango físico del sensor."""


class BateriaAgotadaError(RuntimeError):
    """Se lanza cuando el sensor no tiene batería suficiente para medir."""


# ---------------------------------------------------------------------------
# Clase padre abstracta
# ---------------------------------------------------------------------------
class Sensor(ABC):
    CONSUMO_POR_LECTURA = 2.5  # % de batería gastado en cada medición

    def __init__(self, id_sensor, ubicacion, bateria=100.0):
        self.__id = id_sensor
        self.__ubicacion = ubicacion
        self.__bateria = max(0.0, min(100.0, bateria))
        self.__historial = []
        self.__rechazadas = 0
        self.__lock = threading.Lock()  # protege el estado si se lee en paralelo

    # --- Propiedades de solo lectura (encapsulamiento) ---------------------
    @property
    def id(self):
        return self.__id

    @property
    def ubicacion(self):
        return self.__ubicacion

    @property
    def bateria(self):
        return self.__bateria

    @property
    def lecturas_rechazadas(self):
        return self.__rechazadas

    def obtener_historial(self):
        """Devuelve una copia inmutable: desde fuera no se puede modificar."""
        return tuple(self.__historial)

    def recargar_bateria(self):
        with self.__lock:
            self.__bateria = 100.0

    # --- Interfaz que cada tipo de sensor debe definir ---------------------
    @property
    @abstractmethod
    def unidad(self):
        pass

    @property
    @abstractmethod
    def rango_valido(self):
        """(min, max) físicamente posible. Fuera de esto, la lectura se rechaza."""

    @property
    @abstractmethod
    def rango_normal(self):
        """(min, max) esperable. Fuera de esto, la lectura se guarda como anormal."""

    @abstractmethod
    def _simular_valor(self, rng):
        """Genera un valor simulado como si viniera del hardware."""

    # --- Lógica común ------------------------------------------------------
    def validar(self, valor):
        minimo, maximo = self.rango_valido
        return minimo <= valor <= maximo

    def es_anormal(self, valor):
        minimo, maximo = self.rango_normal
        return not (minimo <= valor <= maximo)

    def tomar_lectura(self, valor=None, rng=random):
        with self.__lock:
            if self.__bateria < self.CONSUMO_POR_LECTURA:
                raise BateriaAgotadaError(f"{self.__id}: batería agotada")

            self.__bateria -= self.CONSUMO_POR_LECTURA
            if valor is None:
                valor = self._simular_valor(rng)

            if not self.validar(valor):
                self.__rechazadas += 1
                raise LecturaInvalidaError(
                    f"{self.__id}: {valor:.1f} {self.unidad} fuera del rango "
                    f"permitido {self.rango_valido}")

            lectura = Lectura(round(valor, 2), datetime.now(), self.es_anormal(valor))
            self.__historial.append(lectura)
            return lectura

    def promedio(self):
        if not self.__historial:
            return None
        return sum(l.valor for l in self.__historial) / len(self.__historial)

    def __str__(self):
        return (f"{self.__class__.__name__}[{self.__id}] en {self.__ubicacion} "
                f"- batería {self.__bateria:.1f}%")


# ---------------------------------------------------------------------------
# Clases hijas
# ---------------------------------------------------------------------------
class SensorTemperatura(Sensor):
    unidad = "°C"
    rango_valido = (-40.0, 85.0)   # límites típicos de un sensor comercial
    rango_normal = (10.0, 35.0)

    def _simular_valor(self, rng):
        r = rng.random()
        if r < 0.05:
            return rng.uniform(90, 120)      # falla del hardware -> inválida
        if r < 0.15:
            return rng.uniform(36, 50)       # pico de calor -> anormal
        return rng.gauss(22, 4)


class SensorHumedad(Sensor):
    unidad = "%"
    rango_valido = (0.0, 100.0)
    rango_normal = (30.0, 70.0)

    def _simular_valor(self, rng):
        r = rng.random()
        if r < 0.05:
            return rng.uniform(-10, -1)      # imposible -> inválida
        if r < 0.15:
            return rng.uniform(80, 98)       # muy húmedo -> anormal
        return rng.gauss(50, 8)


class SensorCalidadAire(Sensor):
    unidad = "AQI"
    rango_valido = (0.0, 500.0)    # escala del Índice de Calidad del Aire
    rango_normal = (0.0, 100.0)    # hasta 100 se considera aceptable

    def _simular_valor(self, rng):
        r = rng.random()
        if r < 0.05:
            return rng.uniform(600, 900)     # inválida
        if r < 0.20:
            return rng.uniform(150, 300)     # contaminación -> anormal
        return abs(rng.gauss(45, 20))


# ---------------------------------------------------------------------------
# Red de sensores: trabaja con cualquier Sensor gracias al polimorfismo
# ---------------------------------------------------------------------------
class RedSensores:
    def __init__(self, umbral_bateria_baja=20.0):
        self.__sensores = {}
        self.umbral_bateria_baja = umbral_bateria_baja
        self.__errores = []

    def agregar(self, sensor):
        if not isinstance(sensor, Sensor):
            raise TypeError("Solo se pueden agregar objetos Sensor")
        if sensor.id in self.__sensores:
            raise ValueError(f"Ya existe un sensor con id {sensor.id}")
        self.__sensores[sensor.id] = sensor

    @property
    def sensores(self):
        return tuple(self.__sensores.values())

    @property
    def errores(self):
        return tuple(self.__errores)

    def _leer(self, sensor, semilla):
        rng = random.Random(semilla)  # un generador por hilo, reproducible
        try:
            sensor.tomar_lectura(rng=rng)
        except (LecturaInvalidaError, BateriaAgotadaError) as e:
            return str(e)
        return None

    def tomar_lecturas_simultaneas(self, ronda):
        """Todos los sensores miden a la vez, cada uno en su propio hilo."""
        with ThreadPoolExecutor(max_workers=len(self.__sensores)) as ejecutor:
            resultados = ejecutor.map(
                self._leer,
                self.__sensores.values(),
                [f"{ronda}-{sid}" for sid in self.__sensores])
        for error in resultados:
            if error:
                self.__errores.append(f"Ronda {ronda}: {error}")

    def sensores_bateria_baja(self):
        return [s for s in self.__sensores.values()
                if s.bateria < self.umbral_bateria_baja]

    def lecturas_anormales(self):
        return [(s, l) for s in self.__sensores.values()
                for l in s.obtener_historial() if l.anormal]

    def reporte_por_tipo(self):
        reporte = {}
        for s in self.__sensores.values():
            datos = reporte.setdefault(s.__class__.__name__,
                                       {"unidad": s.unidad, "valores": [],
                                        "sensores": 0, "rechazadas": 0})
            datos["sensores"] += 1
            datos["rechazadas"] += s.lecturas_rechazadas
            datos["valores"].extend(l.valor for l in s.obtener_historial())
        return reporte

    def imprimir_reporte(self):
        linea = "=" * 78
        print(linea)
        print("REPORTE AGREGADO POR TIPO DE SENSOR".center(78))
        print(linea)
        print(f"{'Tipo':<20}{'Sensores':>9}{'Lecturas':>10}{'Rechaz.':>9}"
              f"{'Mín':>9}{'Prom':>9}{'Máx':>9}  Unidad")
        for tipo, d in self.reporte_por_tipo().items():
            v = d["valores"]
            if v:
                print(f"{tipo:<20}{d['sensores']:>9}{len(v):>10}{d['rechazadas']:>9}"
                      f"{min(v):>9.1f}{sum(v)/len(v):>9.1f}{max(v):>9.1f}  {d['unidad']}")

        print(f"\n{'DETALLE POR SENSOR':-^78}")
        for s in self.__sensores.values():
            prom = s.promedio()
            prom_txt = f"{prom:7.1f} {s.unidad}" if prom is not None else "sin datos"
            print(f"{s.id:<8}{s.__class__.__name__:<20}{s.ubicacion:<22}"
                  f"bat {s.bateria:5.1f}%   prom {prom_txt}")

        print(f"\n{'SENSORES CON BATERÍA BAJA (< ' + str(self.umbral_bateria_baja) + '%)':-^78}")
        bajos = self.sensores_bateria_baja()
        for s in bajos:
            print(f"  ⚠ {s}")
        if not bajos:
            print("  Ninguno")

        anormales = self.lecturas_anormales()
        print(f"\n{'LECTURAS ANORMALES (' + str(len(anormales)) + ')':-^78}")
        for s, l in anormales:
            minimo, maximo = s.rango_normal
            print(f"  {s.id:<8}{s.ubicacion:<22}{l.valor:>8.1f} {s.unidad:<4}"
                  f" (normal: {minimo}-{maximo})")

        print(f"\n{'LECTURAS RECHAZADAS / ERRORES (' + str(len(self.__errores)) + ')':-^78}")
        for e in self.__errores:
            print(f"  ✗ {e}")
        print(linea)


# ---------------------------------------------------------------------------
# Simulación
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    red = RedSensores(umbral_bateria_baja=20)

    red.agregar(SensorTemperatura("T-01", "Invernadero norte"))
    red.agregar(SensorTemperatura("T-02", "Invernadero sur", bateria=35))
    red.agregar(SensorTemperatura("T-03", "Depósito"))
    red.agregar(SensorTemperatura("T-04", "Oficina central", bateria=12))
    red.agregar(SensorHumedad("H-01", "Invernadero norte"))
    red.agregar(SensorHumedad("H-02", "Invernadero sur"))
    red.agregar(SensorHumedad("H-03", "Depósito", bateria=28))
    red.agregar(SensorHumedad("H-04", "Sótano"))
    red.agregar(SensorCalidadAire("A-01", "Estacionamiento"))
    red.agregar(SensorCalidadAire("A-02", "Oficina central"))
    red.agregar(SensorCalidadAire("A-03", "Planta de producción", bateria=40))
    red.agregar(SensorCalidadAire("A-04", "Entrada principal"))

    RONDAS = 8
    for ronda in range(1, RONDAS + 1):
        red.tomar_lecturas_simultaneas(ronda)

    print(f"Red de {len(red.sensores)} sensores - {RONDAS} rondas de lectura\n")
    red.imprimir_reporte()

    # --- Demostración del encapsulamiento ---------------------------------
    print("\nPRUEBAS DE ENCAPSULAMIENTO")
    sensor = red.sensores[0]
    try:
        sensor.bateria = 100
    except AttributeError:
        print("  ✓ No se puede asignar la batería directamente")

    historial = sensor.obtener_historial()
    try:
        historial.append("dato falso")
    except AttributeError:
        print("  ✓ El historial devuelto no se puede modificar")

    try:
        historial[0].valor = 999
    except AttributeError:
        print("  ✓ Una lectura guardada no se puede alterar")

    try:
        sensor.tomar_lectura(valor=150)
    except LecturaInvalidaError as e:
        print(f"  ✓ Validación manual: {e}")

    sensor.recargar_bateria()
    print(f"  ✓ Batería recargada mediante el método público: {sensor.bateria}%")