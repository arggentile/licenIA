from datetime import datetime


class Venta:
    """
    Representa una venta puntual registrada en el sistema.
    """
    def __init__(self, codigo_venta, codigo_producto, cantidad, precio_unitario, costo_unitario, fecha_venta):
        Venta._validar_datos_iniciales(codigo_venta, codigo_producto, cantidad, precio_unitario, costo_unitario, fecha_venta)
       
        self._codigo_venta = codigo_venta
        self._codigo_producto = codigo_producto
        self._cantidad = cantidad
        self._precio_unitario = float(precio_unitario) # precio de venta
        self._costo_unitario = float(costo_unitario) # costo del items
        self._fecha_venta = fecha_venta

    @staticmethod
    def _es_fecha_valida(fecha: str):
        try:
            datetime.strptime(fecha, "%d-%m-%Y")
            return True
        except ValueError:
            return False
        
    @staticmethod 
    def _validar_datos_iniciales(codigo_venta, codigo_producto, cantidad, precio_unitario, costo_unitario, fecha_venta):
        """ Realiza una validacion de algunos datos iniciales"""
        if not isinstance(codigo_venta, int) or codigo_venta <= 0:
            raise ValueError("El codigo de venta debe ser positivo.")

        
        if not isinstance(cantidad, int) or cantidad <= 0:
            raise ValueError("La cantidad debe ser positiva.")

        if not isinstance(codigo_producto, int) or codigo_producto <= 0:
            raise ValueError("El codigo de producto debe ser positivo.")

        if not isinstance(precio_unitario, (int, float)) or float(precio_unitario) <= 0.0:
            raise ValueError("El precio debe ser un valor numerico decimal. Ingrese un precio positivo")

        if not isinstance(costo_unitario, (int, float)) or costo_unitario<=0:
            raise ValueError("El costo unitario debe ser un valor numerico decimal. Ingrese un costo positivo")
                
        if not Venta._es_fecha_valida(fecha_venta):
            raise ValueError("Fecha de Venta Invalida.")    


    def get_codigo_producto(self):
        return self._codigo_producto

    def get_codigo_venta(self):
        return self._codigo_venta

    def get_cantidad_vendida(self):
        return self._cantidad

    def get_precio_unitario(self):
        return self._precio_unitario

    def get_fecha_venta(self):
        return self._fecha_venta

    def get_costo_unitario(self):
        return self._costo_unitario
    

    def valor_total_venta(self):
        """Devuelve el total facturado por esta venta."""
        return self._cantidad * self._precio_unitario

    def __str__(self):
        return (f"Id Venta: {self._codigo_venta} | "
                f"Fecha: {self._fecha_venta} | "
                f"Prod: {self._codigo_producto} | "
                f"Cant: {self._cantidad} | "
                f"P.Unit: ${self._precio_unitario:.2f} | "
                f"Costo.Unit: ${self._costo_unitario:.2f} | "
                f"Total: ${self.valor_total_venta():.2f}")  
 
if __name__ == '__main__':
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

    

        