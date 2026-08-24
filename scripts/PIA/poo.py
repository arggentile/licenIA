class Perro:
    def __init__(self, nombre, raza, edad):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad

    def ladrar(self):
        return f"{self.nombre} dice: ¡Guau guau!"

    def cumplir_años(self):
        self.edad += 1  
        return f"{self.nombre} ahora tiene {self.edad} años"

    def describir(self):
        return f"{self.nombre} es un {self.raza} de {self.edad} años"