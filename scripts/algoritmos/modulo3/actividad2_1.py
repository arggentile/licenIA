class vehiculo:
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

class Moto(vehiculo):
    def __init__(self, marca, modelo, anio, velocidad):
        super().__init__(marca, modelo, anio, velocidad)