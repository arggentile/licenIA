class Producto:
    def __init__(self, nombre, precio, stock = 0):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def sumar_stock(self, cantidad):
        self.stock += cantidad

    def reducir_stock(self, cantidad):
        if(self.stock<cantidad):
            print("no hay stock suficiente")
            return
        self.stock -= cantidad

    def vender(self, cantidad):
        if cantidad <= 0:
            print(f"Cantidad debe ser positiva, mayor a cero productos.")
            return False
        if cantidad > self.stock:
            print(f"No hay stock suficiente. La cantidad en stock es {self.stock}")
            return False
        self.reducir_stock(cantidad)
        total = cantidad * self.precio
        print(f"El total a pagar es: {total}")
        return True
    
    def aplicar_descuento(self, descuento):
        if descuento <= 0 or descuento >= 100:
            print(f"Descuento debe estar entre 0 y 100")
            return False
        precio_anterior = self.precio
        self.precio = self.precio * (1 - descuento / 100)
        return True
    
    def info(self):
        print(f"EL nombre del producto es {self.nombre} el precio es {self.precio}  el stock es {self.stock}")        
        
class Inventario:
        def __init__(self):
            self.productos = [] # cambiar por algo más efecftivo 

        def existe_producto(self, nombre):
            existe = False
            posicionProducto = None
            for posicion, ppr in  enumerate(self.productos):
                if ppr.nombre == nombre:
                    existe = True
                    posicionProducto = posicion
            
            return existe, posicionProducto
            
        
        def agregar_producto(self, nuevoProducto):
            existe, posicion_producto = self.existe_producto(nuevoProducto) 
            if(existe == False):
                self.productos.append(nuevoProducto)
            else: #actualizamos stock
                productoIntv = self.productos[posicion_producto] #accedemos a lproducto ya en el inventario 
                productoIntv.sumar_stock(nuevoProducto.stock) 

        def vender_producto(self, nombreProducto, cantidad):
            existe, posicion_producto = self.existe_producto(nombreProducto) 
            if(existe == False):
                return f"No existe el producto a vender"
            else: #actualizamos stock
                elProducto = self.productos[posicion_producto] #accedemos al producto ya en el inventario 
                elProducto.vender(cantidad)  

        def info(self):
            if( len(self.productos) > 0):
                for posicion, elProducto in  enumerate(self.productos):  
                    elProducto.info()

                
        

miInventario = Inventario()
producto1 = Producto("Yerba", 1500, 1000)
producto2 = Producto("Mate", 1000, 1500)
producto3 = Producto("Azucar", 750, 500)

miInventario.agregar_producto(producto1)
miInventario.agregar_producto(producto2)
miInventario.agregar_producto(producto3)
miInventario.info()

miInventario.vender_producto("Yerba", 500)
miInventario.info()
miInventario.vender_producto("Yerba", 300)
miInventario.info()
miInventario.vender_producto("Yerba", 600)
miInventario.info()

