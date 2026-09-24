class Vehiculo:
    def __init__(self, marca, modelo, anio, velocidad):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.velocidad = velocidad

    def aumentar_velocidad(self, velocidad):
        self.velocidad+=velocidad

    def disminuir_velocidad(self, velocidad):
        if self.velocidad < 0:
            print("Se ha llegado  la velocidad minima, no puede bajar más")
            return
        if self.velocidad<velocidad:
            print("No puede bajar la velocidad mencionada, no hay velñocidad suficiente para regitrar el cmbio.")
            return
        self.velocidad-=velocidad

    def info(self):
        return f"Marca es {self.marca} modelo es: {self.modelo} año es: {self.anio} velocidad es: {self.velocidad}"    

class Moto(Vehiculo):
    def __init__(self, marca, modelo, anio, velocidad, cilindrada):
        super().__init__(marca, modelo, anio, velocidad)
        self.cilindrada = cilindrada

class Auto(Vehiculo):
    def __init__(self, marca, modelo, anio, velocidad, cant_puertas):
        super().__init__(marca, modelo, anio, velocidad)
        self.cantidad_puertas = cant_puertas

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

