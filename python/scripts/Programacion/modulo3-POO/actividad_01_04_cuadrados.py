class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)

    def es_cuadrado(self):
        return self.base == self.altura

    def escalar(self, factor_escala):
        self.altura *=  factor_escala
        self.base *=  factor_escala

    def mostrar_info(self):
        print(f"La base es: {self.base} la altura es: {self.altura} el area es: {self.calcular_area()} el perimetro es: {self.calcular_perimetro()}")

rectangulo1 = Rectangulo(2,4)
rectangulo1.mostrar_info()
rectangulo1.escalar(2)
rectangulo1.mostrar_info()
if(rectangulo1.es_cuadrado()):
    print("Es cuadrado")
else:
    print("No es cuadrado")   


rectangulo2 = Rectangulo(3,3)
rectangulo2.mostrar_info()
rectangulo2.escalar(2)
rectangulo2.mostrar_info()
if(rectangulo2.es_cuadrado()):
    print("Es cuadrado")
else:
    print("No es cuadrado")   
     
