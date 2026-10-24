class Empleado:
    def __init__(self, nro_empleado, nombre, salario_base):
        self.nro_empleado = nro_empleado
        self.nombre = nombre
        self.salario_base = salario_base

    def calcular_salario(self):
        return self.salario_base

    def info(self):
        return f"Numero de Empleado: {self.nro_empleado} nombre es: {self.nombre} Salario Base es: {self.salario_base}"    

class EmpĺeadoTC(Empleado):
    def __init__(self, nro_empleado, nombre, salario_base, bonificacion):
        super().__init__( nro_empleado, nombre, salario_base)
        self.bonificacion = bonificacion

    def calcular_salario(self):
        return self.salario_base + (self.salario_base * self.bonificacion)


class EmpleadoXHora(Empleado):
    def __init__(self, nro_empleado, nombre, salario_base, tarifa_base, cant_horas):
        super().__init__(nro_empleado, nombre, salario_base)
        self.cant_horas = cant_horas
        self.tarifa_base = tarifa_base

    def info(self):
        info = super().info()
        return info + f"Cantidad de puertas {self.cantidad_puertas}"

class Camion(Vehiculo):
    def __init__(self, marca, modelo, anio, velocidad, cant_puertas, capacidad_carga, cargado):
        super().__init__(marca, modelo, anio, velocidad)
        self.capacidad_carga = capacidad_carga
        self.cargado = cargado

if __name__ == "__main__":
    moto1= Moto("Suzuki", 'Nakeds' , 1998, 180, 4)
    moto2= Moto('Honda', 'XR300L', 2020, 220, 110)

    auto1= Auto('Suzuki', 'Toyota', 2022, 220, 4)
    print(auto1.info())

