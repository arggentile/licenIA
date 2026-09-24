class Libro:
    def __init__(self, titulo, autor, anio, disponible = True):
        self.titulo = titulo
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
        self.disponible = disponible

    def prestar(self):
        if self.disponible:
            self.disponible = False
        else:
            print("Libro no disponible")

    def devolver(self):
        if self.disponible == False:
            self.disponible = True
        else:
            print("El libro no esta prestado")

    def info(self):
        print(f"El tiutlo del libro es {self.titulo} el año de publicacion es {self.anio} el autor es: {self.autor}")
        if self.disponible:
            print(f"El libro esta disponible")
        else:
            print(f"libro prstado")

libro1 = Libro("El señor de los anillos 1", "juanito peres", 2000)
libro2 = Libro("El señor de los anillos 2", "H cabral", 2002)
libro3 = Libro("El señor de los anillos 3", "lucho Olivera", 2000)

libro1.info()
libro2.info()
libro3.info()

libro1.prestar()
libro1.info()
libro1.devolver()
libro1.info()
    
        
        