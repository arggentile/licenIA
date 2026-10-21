"""
Módulo: producto.py
Descripción: Define la clase Producto, que representa un artículo del inventario.
Aplica encapsulamiento mediante atributos "privados" (prefijo _) y expone
propiedades (getters/setters) controladas.
"""


class Producto:
    """
    Representa un producto del inventario del negocio.

    Atributos encapsulados:
        _codigo (str): Identificador único del producto.
        _nombre (str): Nombre descriptivo.
        _precio_venta (float): Precio unitario de venta.
        _costo (float): Costo unitario de compra/producción.
        _stock_actual (int): Cantidad disponible en inventario.
        _categoria (str): Categoría a la que pertenece.
    """

    def __init__(self, codigo, nombre, precio_venta, costo,
                 stock_actual=0, categoria="General"):
        # Validaciones básicas de los datos de entrada
        if precio_venta < 0 or costo < 0:
            raise ValueError("El precio de venta y el costo no pueden ser negativos.")
        if stock_actual < 0:
            raise ValueError("El stock no puede ser negativo.")

        self._codigo = str(codigo).strip().upper()
        self._nombre = str(nombre).strip()
        self._precio_venta = float(precio_venta)
        self._costo = float(costo)
        self._stock_actual = int(stock_actual)
        self._categoria = str(categoria).strip().title()

    # ------------------- Propiedades (encapsulamiento) ------------------- #
    @property
    def codigo(self):
        return self._codigo

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        if not nuevo_nombre:
            raise ValueError("El nombre no puede estar vacío.")
        self._nombre = str(nuevo_nombre).strip()

    @property
    def precio_venta(self):
        return self._precio_venta

    @precio_venta.setter
    def precio_venta(self, nuevo_precio):
        if nuevo_precio < 0:
            raise ValueError("El precio de venta no puede ser negativo.")
        self._precio_venta = float(nuevo_precio)

    @property
    def costo(self):
        return self._costo

    @costo.setter
    def costo(self, nuevo_costo):
        if nuevo_costo < 0:
            raise ValueError("El costo no puede ser negativo.")
        self._costo = float(nuevo_costo)

    @property
    def stock_actual(self):
        return self._stock_actual

    @property
    def categoria(self):
        return self._categoria

    # ------------------- Métodos de negocio ------------------- #
    def ganancia_unitaria(self):
        """Devuelve la ganancia por unidad vendida."""
        return self._precio_venta - self._costo

    def margen_porcentaje(self):
        """Devuelve el margen de ganancia como porcentaje sobre el costo."""
        if self._costo == 0:
            return 0.0
        return (self.ganancia_unitaria() / self._costo) * 100

    def aumentar_stock(self, cantidad):
        """Suma unidades al stock. Usado al reponer inventario."""
        if cantidad <= 0:
            raise ValueError("La cantidad a aumentar debe ser positiva.")
        self._stock_actual += int(cantidad)

    def disminuir_stock(self, cantidad):
        """
        Resta unidades del stock. Usado al concretar una venta.
        Lanza error si no hay stock suficiente.
        """
        if cantidad <= 0:
            raise ValueError("La cantidad a disminuir debe ser positiva.")
        if cantidad > self._stock_actual:
            raise ValueError(
                f"Stock insuficiente. Disponible: {self._stock_actual}, "
                f"solicitado: {cantidad}."
            )
        self._stock_actual -= int(cantidad)

    def __str__(self):
        return (f"[{self._codigo}] {self._nombre} | Cat: {self._categoria} | "
                f"Precio: ${self._precio_venta:.2f} | Costo: ${self._costo:.2f} | "
                f"Stock: {self._stock_actual}")

    def to_dict(self):
        """Serializa el producto a diccionario (útil para persistencia)."""
        return {
            "codigo": self._codigo,
            "nombre": self._nombre,
            "precio_venta": self._precio_venta,
            "costo": self._costo,
            "stock_actual": self._stock_actual,
            "categoria": self._categoria,
        }
