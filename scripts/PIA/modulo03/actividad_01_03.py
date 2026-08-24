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
            print(f"Cno hay stock suficiente. La cantidad en stock es {self.stock}")
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
            
        
class Inventario:
        def __init__(self, productos = []):
            self.productos = productos #lista de productos

        def existe_producto(self, producto):
            existe = False
            posicionProducto = None
            for posicion, ppr in  enumerate(self.productos):
                if ppr.nombre == producto.nombre:
                    existe = True
                    posicionProducto = posicion
            
            return posicionProducto
            
        
        def agregar_producto(self, nuevoProducto):
            posiproducto = self.existe_producto(nuevoProducto) 
            if(posiproducto == None):
                self.productos.append(nuevoProducto)
            else: #actualizamos stock
                productoIntv = self.productos[posiproducto] #accedemos alproducto ya en el inventario 
                productoIntv.sumar_stock(nuevoProducto.stock) 
                self.productos[posiproducto] = productoIntv

        
        

cuentaJuan = Cuenta(1001, "juan Esteban")
cuentaMariana   = Cuenta(1001, "Mariana")
cuentaJuan.mostrar_info();
cuentaJuan.deposito(1000)
cuentaJuan.deposito(500)
cuentaJuan.mostrar_info()
cuentaJuan.retirar(1000)
cuentaJuan.mostrar_info()
cuentaJuan.retirar(1000)
cuentaJuan.mostrar_info()


