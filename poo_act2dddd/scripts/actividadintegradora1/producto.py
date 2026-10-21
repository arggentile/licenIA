class Producto:
    """
    Representa un producto del negocio.
    """
    
    def __init__(self, codigo_producto, nombre, categoria, precio_venta, costo_unitario, stock_actual):
        if not self.es_codigo_producto_valido(codigo_producto):
            raise ValueError("El codigo_producto del producto debe ser numerico.")
        
        self._codigo_producto = codigo_producto
        self.categoria = categoria
        self.nombre = nombre
        self._stock_actual = stock_actual
       
        if not self.es_precio_valido(precio_venta):
            raise ValueError("El precio de venta debeser positivo.")
        self._precio_venta = float(precio_venta)
       
        if not self.es_precio_valido(costo_unitario):
            raise ValueError("El costo unitario debe ser positivo.")
        self._costo_unitario = float(costo_unitario)
    
    @staticmethod
    def es_codigo_producto_valido(codigo_producto):
        if not isinstance(codigo_producto, int):
            return False
        return True

    @staticmethod
    def es_precio_valido(precio):
        if not isinstance(precio,  (int, float)):
            return False
        return precio > 0


    # ------------------- Propiedades (encapsulamiento) ------------------- #
    def get_codigo_producto(self):
        return self._codigo_producto

    def get_precio_venta(self):
        return self._precio_venta
    
    def get_costo_unitario(self):
        return self._costo_unitario

    def get_stock_actual(self):
        return self._stock_actual

    def set_precio_venta(self, nuevo_precio):
        if nuevo_precio < 0:
            raise ValueError("El precio de venta no puede ser negativo.")
        self._precio_venta = float(nuevo_precio)

    def set_costo_unitario(self, nuevo_costo):
        if nuevo_costo < 0:
            raise ValueError("El costo no puede ser negativo.")
        self._costo_unitario = float(nuevo_costo)

    def disminuir_stock_actual(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad a aumentar debe ser positiva.")
        if (self.stock_actual - cantidad) < 0:
            raise ValueError("No se puede registrar la disminución del stcock, no hay tantos productos disponibles.")
        self._stock_actual -= cantidad
        
    def aumentar_stock_actual(self, cantidad):
        if not isinstance(cantidad, int):
            raise ValueError("La cantidad a aumentar el stock debe ser poositiva.")
        if cantidad <= 0:
            raise ValueError("La cantidad a aumentar el stock debe ser poositiva..")
        self._stock_actual += cantidad

    def ganancia_unitaria(self):
        return self._precio_venta - self._costo_unitario

    def info(self):
        print(f" Información del producto: codigo_producto: {self._codigo_producto}  Nombre: {self.nombre} Categroria: {self.categoria} Precio Venta: {self._precio_venta} Costo Unitario: {self._costo_unitario} stock_actual: {self._stock_actual}")

    def __str__(self):
        return (f"[{self._codigo_producto}] {self.nombre} | Cat: {self.categoria} | "
                f"Precio: ${self._precio_venta:.2f} | Costo: ${self._costo_unitario:.2f} | "
                f"stock_actual: {self._stock_actual} | Ganancia: ${self.ganancia_unitaria():.2f}")

if __name__ == '__main__':
    producto_detergente = Producto(100, "Detergente Ala", "LIMPIEZA", 1200.0, 850.50, 1000)
    producto_lavavajillas = Producto(101, "Lava Vajillas", "LIMPIEZA", 22000, 1500.50 , 1000)
    producto_yerba = Producto(102, "Yerba", "ALMACEN", 4000.0, 1850.50, 1000)

    print(f"Mostrando informaión de los productos: ")
    producto_detergente.info()
    producto_lavavajillas.info()
    producto_yerba.info()

    print(f"{producto_detergente.__str__()}")
    print(f"{producto_lavavajillas.__str__()}")
    print(f"{producto_yerba.__str__()}")


    print(f"Info detallada:")
    print(f"El identificador del producto Yerba es: {producto_yerba.get_codigo_producto()}")
    print(f"El identificador del producto Detergente es: {producto_detergente.get_codigo_producto()}")

    print(f"El precio unitario del producto Yerba es: {producto_yerba.get_precio_venta()}")
    print(f"El precio unitario del producto Detergente es: {producto_detergente.get_precio_venta()}")

    print(f"El costo unitario del producto Yerba es: {producto_yerba.get_costo_unitario()}")
    print(f"El costo unitario del producto Detergente es: {producto_detergente.get_costo_unitario()}")

    print(f"El stock_actual del producto Yerba es: {producto_yerba.get_stock_actual()}")
    print(f"El stock_actual del producto Detergente es: {producto_detergente.get_stock_actual()}")


"""




    def to_dict(self):
        return {
            "codigo_producto": self._codigo_producto,
            "nombre": self._nombre,
            "precio_venta": self._precio_venta,
            "costo": self._costo,
            "stock_actual_actual": self._stock_actual_actual,
            "categoria": self._categoria,
        }
"""
                         
   