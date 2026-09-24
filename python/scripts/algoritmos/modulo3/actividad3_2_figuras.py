import math


class Figura():
    """Clase padre abstracta: define la interfaz común de todas las figuras 3D."""
 
    def __init__(self, nombre):
        self.nombre = nombre
 
    def volumen(self):
        return None
 
    def area_superficie(self):
        return None
 
    @staticmethod
    def _validar_positivo(valor, nombre_dato):
        if valor <= 0:
            raise ValueError(f"El {nombre_dato} debe ser mayor que 0 (recibido: {valor})")
        return valor
 
    def __str__(self):
        return (f"{self.nombre:<30} Volumen: {self.volumen():>10.2f}   "
                f"Área: {self.area_superficie():>10.2f}")
 
 
class Cubo(Figura):
    def __init__(self, lado):
        super().__init__(f"Cubo (lado={lado})")
        self.lado = self._validar_positivo(lado, "lado")
 
    def volumen(self):
        return self.lado ** 3
 
    def area_superficie(self):
        return 6 * self.lado ** 2
 
 
class Esfera(Figura):
    def __init__(self, radio):
        super().__init__(f"Esfera (radio={radio})")
        self.radio = self._validar_positivo(radio, "radio")
 
    def volumen(self):
        return (4 / 3) * math.pi * self.radio ** 3  # noqa: F821
 
    def area_superficie(self):
        return 4 * math.pi * self.radio ** 2
 
 
class Cilindro(Figura):
    def __init__(self, radio, altura):
        super().__init__(f"Cilindro (radio={radio}, altura={altura})")
        self.radio = self._validar_positivo(radio, "radio")
        self.altura = self._validar_positivo(altura, "altura")
 
    def volumen(self):
        return math.pi * self.radio ** 2 * self.altura
 
    def area_superficie(self):
        return 2 * math.pi * self.radio * (self.radio + self.altura)
 
 
class ColeccionFiguras:
    """Agrupa figuras de cualquier tipo y calcula totales usando polimorfismo."""
 
    def __init__(self):
        self.figuras = []
 
    def agregar(self, figura):
        if not isinstance(figura, Figura):
            raise TypeError("Solo se pueden agregar objetos de tipo Figura")
        self.figuras.append(figura)
 
    def volumen_total(self):
        # Cada figura sabe calcular su propio volumen: no importa de qué clase sea
        return sum(f.volumen() for f in self.figuras)
 
    def area_total(self):
        return sum(f.area_superficie() for f in self.figuras)
 
    def mostrar(self):
        print("=" * 75)
        for figura in self.figuras:
            print(figura)
        print("-" * 75)
        print(f"{'TOTAL':<30} Volumen: {self.volumen_total():>10.2f}   "
              f"Área: {self.area_total():>10.2f}")
        print("=" * 75)
 
 
if __name__ == "__main__":
    coleccion = ColeccionFiguras()
    coleccion.agregar(Cubo(3))
    coleccion.agregar(Esfera(2))
    coleccion.agregar(Cilindro(1.5, 4))
    coleccion.agregar(Cubo(1))
    coleccion.agregar(Esfera(0.5))
 
    coleccion.mostrar()
 
    # Demostración de la validación
    try:
        Cubo(-2)
    except ValueError as e:
        print(f"\nError esperado: {e}")
 
    # Demostración de que la clase abstracta no se puede instanciar
    try:
        Figura("genérica")
    except TypeError as e:
        print(f"Error esperado: {e}")
 