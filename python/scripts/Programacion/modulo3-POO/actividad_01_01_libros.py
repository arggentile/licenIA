class Libro:
    def __init__(self, titulo, autor, anio):
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
        self.disponible = True


    def prestar(self):
        if(self.disponible):
            self.disponible = False
        else:
            print("Eror no disponible")
            return None

    def regresar(self):
        self.disponible += True

    def esta_disponible(self):
        return self.disponible
    
    def mostrar_info(self):
        print(f"Datode del libro son: Nombre: {self.titulo}, autor: {self.autor} año: {self.anio}")


libro1 = Libro("Orgullo y prejuicio", "Jane Austen", 1998)   
libro2 = Libro("Crimen y castigo", "Fiódor Dostoyevski", 2001)   
libro3 = Libro("La Odisea", "Homero", 1954)   
libro4 = Libro("El Señor de los Anillos", "J. R. R. Tolkien",1975)   
libro1.mostrar_info();
libro2.mostrar_info();
libro3.mostrar_info();
libro4.mostrar_info();
libro1.prestar()
if(libro1.esta_disponible() == False):
    print("libro NO disponible")
libro1.regresar()
if(libro1.esta_disponible()):
    print("libro disponible")



           