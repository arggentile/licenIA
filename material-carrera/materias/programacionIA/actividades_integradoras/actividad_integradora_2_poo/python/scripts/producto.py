class Producto:
    """
    Representa un producto del negocio.
    """
    
    def __init__(self, codigo_producto, nombre, categoria, precio_venta, costo_unitario, stock_actual):
        Producto.validar_datos_iniciales(codigo_producto, nombre, categoria, precio_venta, costo_unitario, stock_actual)
        
        self._codigo_producto = codigo_producto
        self.categoria = categoria
        self.nombre = nombre
        self._stock_actual = stock_actual
        self._precio_venta = float(precio_venta)
        self._costo_unitario = float(costo_unitario)
    
    @staticmethod
    def validar_datos_iniciales(codigo_producto, nombre, categoria, precio_venta, costo_unitario, stock_actual):
        if not Producto.es_codigo_producto_valido(codigo_producto):
            raise ValueError("El codigo_producto del producto debe ser numerico.")
        
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El nombre no puede estar vacío.")

        if not isinstance(categoria, str) or not categoria.strip():
            raise ValueError("La categoria no puede estar vacía.")
        
        if not Producto.es_precio_valido(precio_venta):
            raise ValueError("El precio de venta debe ser positivo.")

        if not Producto.es_precio_valido(costo_unitario):
            raise ValueError("El costo unitario debe ser positivo.")    

        if not isinstance(stock_actual, int) or stock_actual < 0:
            raise ValueError("El stock debe ser positivo.")  
        
    @staticmethod
    def es_codigo_producto_valido(codigo_producto):
        """ Analiza si un codigo es valido o no"""
        return isinstance(codigo_producto, int) and codigo_producto > 0

    @staticmethod
    def es_precio_valido(precio):
        """ Analiza si un precio es valido o no"""
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
        if not Producto.es_precio_valido(nuevo_precio):
            raise ValueError("El precio de venta debe ser positivo.")
        self._precio_venta = float(nuevo_precio)

    def set_costo_unitario(self, nuevo_costo):
        if not Producto.es_precio_valido(nuevo_costo):
            raise ValueError("El costo unitario de venta debe ser positivo.")
        self._costo_unitario = float(nuevo_costo)

    def disminuir_stock_actual(self, cantidad):
        """ Disminuye el stock actual del producto en la cantidad informada"""
        if not isinstance(cantidad, int):
            raise ValueError("La cantidad a disminuir el stock debe ser positiva.")
        if cantidad <= 0:
            raise ValueError("La cantidad a disminuir debe ser positiva.")
        if (self._stock_actual - cantidad) < 0:
            raise ValueError("No se puede registrar la disminución del stock, no hay tantos productos disponibles.")
        self._stock_actual -= cantidad
        
    def aumentar_stock_actual(self, cantidad):
        """ Aumenta el stock actual del producto en la cantidad informada"""
        if not isinstance(cantidad, int):
            raise ValueError("La cantidad a aumentar el stock debe ser positiva.")
        if cantidad <= 0:
            raise ValueError("La cantidad a aumentar el stock debe ser positiva.")
        self._stock_actual += cantidad

    def ganancia_unitaria(self):
        """ Devuelve la ganancia obtenida del producto, consecuencia de la diferencia entre el precio de venta y el costo"""
        return self._precio_venta - self._costo_unitario

    def __str__(self):
        return (f"[{self._codigo_producto}] {self.nombre} | Cat: {self.categoria} | "
                f"Precio: ${self._precio_venta:.2f} | Costo: ${self._costo_unitario:.2f} | "
                f"stock_actual: {self._stock_actual} | Ganancia: ${self.ganancia_unitaria():.2f}")

if __name__ == '__main__':
    producto_detergente = Producto(100, "Detergente Ala", "LIMPIEZA", 1200.0, 850.50, 1000)
    producto_lavavajillas = Producto(101, "Lava Vajillas", "LIMPIEZA", 22000, 1500.50 , 1000)
    producto_yerba = Producto(102, "Yerba", "ALMACEN", 4000.0, 1850.50, 1000)

    print(f"Mostrando información de los productos: ")

    print(f"{producto_detergente}")
    print(f"{producto_lavavajillas}")
    print(f"{producto_yerba}")


    print(f"Info detallada:")
    print(f"El identificador del producto Yerba es: {producto_yerba.get_codigo_producto()}")
    print(f"El identificador del producto Detergente es: {producto_detergente.get_codigo_producto()}")

    print(f"El precio unitario del producto Yerba es: {producto_yerba.get_precio_venta()}")
    print(f"El precio unitario del producto Detergente es: {producto_detergente.get_precio_venta()}")

    print(f"El costo unitario del producto Yerba es: {producto_yerba.get_costo_unitario()}")
    print(f"El costo unitario del producto Detergente es: {producto_detergente.get_costo_unitario()}")

    print(f"El stock_actual del producto Yerba es: {producto_yerba.get_stock_actual()}")
    print(f"El stock_actual del producto Detergente es: {producto_detergente.get_stock_actual()}")