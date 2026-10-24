class Forma:
    def __init__(self, nombre):
        self.nombre = nombre
    def calcular_area(self):
        return 0
    def describir(self):
        return f"{self.nombre} con área {self.calcular_area():.2f}"

class Rectangulo(Forma):
    def __init__(self, base, altura):
        super().__init__("Rectángulo")
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

class Circulo(Forma):
    def __init__(self, radio):
        super().__init__("Círculo")
        self.radio = radio

    def calcular_area(self):
        return 3.14159 * (self.radio ** 2)

class Triangulo(Forma):
    def __init__(self, base, altura):
        super().__init__("Triángulo")
        self.base = base
        self.altura = altura

        def calcular_area(self):
            return (self.base * self.altura) / 2

def calcular_area_total(formas):
    total = 0
    for forma in formas:
        area = forma.calcular_area()
        print(forma.describir())
        total += area
    return total

formas = [ Rectangulo(10, 5), Circulo(7), Triangulo(8, 6), Rectangulo(15, 3) ]
print(f"\nÁrea total: {calcular_area_total(formas):.2f}")      