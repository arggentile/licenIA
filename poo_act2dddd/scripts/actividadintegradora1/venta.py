from datetime import datetime


class Venta:
    """
    Representa una venta puntual registrada en el sistema.

    Atributos:
        _codigo_producto (str): Código del producto vendido.
        _cantidad (int): Unidades vendidas.
        _precio_unitario (float): Precio al que se vendió cada unidad.
        _fecha (datetime): Fecha en la que ocurrió la venta.
    """
    def __init__(self, codigo_venta, codigo_producto, cantidad, precio_unitario, valor_unitario, fecha_venta):
        self._validar_datos_iniciales(cantidad, precio_unitario, fecha_venta)

       
        self._codigo_venta = codigo_venta
        self._codigo_producto = codigo_producto
        self._cantidad = cantidad
        self._precio_unitario = float(precio_unitario)
        self._valor_unitario = float(valor_unitario)
        self._fecha_venta = fecha_venta

    @staticmethod
    def _es_fecha_valida(fecha: str):
        try:
            datetime.strptime(fecha, "%d-%m-%Y")
            return True
        except ValueError:
            return False

    def _validar_datos_iniciales(self, cantidad, precio_unitario, fecha_venta):
        if not isinstance(cantidad, int):
            raise ValueError("La cantidad debe ser positiva.")
        
        if not isinstance(precio_unitario, float):
            raise ValueError("El valor debe ser un valor numerico decimal.")

        if not self._es_fecha_valida(fecha_venta):
            raise ValueError("Fecha de Venta Invalida.")
        
        return True


    def get_codigo_producto(self):
        return self._codigo_producto

    def get_codigo_venta(self):
            return self.get_codigo_venta

    def get_cantidad_vendida(self):
        return self._cantidad

    def get_precio_unitario(self):
        return self._precio_unitario

    def get_fecha_venta(self):
        return self._fecha_venta

    def get_valor_unitario(self):
            return self._valor_unitario
    

    def valor_total_venta(self):
        """Devuelve el total facturado por esta venta."""
        return self._cantidad * self._precio_unitario

    def __str__(self):
        return (f"Id Venta: {self._codigo_venta:.5f} | "
                f"Fecha{self._fecha_venta} | "
                f"Prod: {self._codigo_producto} | "
                f"Cant: {self._cantidad} | "
                f"P.Unit: ${self._precio_unitario:.2f} | "
                f"Valor.Unit: ${self._valor_unitario:.2f} | "
                f"Total: ${self.valor_total_venta():.2f}")  
 
if __name__ == '__main__':
    """
    try:
        print(f"Chequeamos la validaciones: ")
        product1 = Venta(101, 50, 1500, 's2026-05-10')
        product2 = Venta(102, "50s", 1500, 's2026-05-10')
    except ValueError:
        print(f"Error Excepcion")
    """    

    try:
        ventas = []
        ventas.append( Venta(10000, 101, 50, 1500.00, 1000.00,'10-05-2026'))
        ventas.append( Venta(10001, 102, 25, 2210.55, 1800.00,'10-06-2026'))
        ventas.append( Venta(10002, 103, 25, 7500.25, 500.25,'05-05-2026'))
        ventas.append( Venta(10003, 101, 15, 1350.33, 1100.00,'12-05-2026'))
        ventas.append( Venta(10004, 101, 15, 3650.22, 3000,'07-06-2026'))
        for i, elem in enumerate(ventas):
            print(f" { elem.__str__() }")
    except ValueError:
        print(f"Error Excepcion")

    

        