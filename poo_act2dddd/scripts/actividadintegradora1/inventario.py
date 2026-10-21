import json
import os

#import numpy as np
import pandas as pd

from producto import Producto
from venta import Venta


class Inventario:
    """
    Administra productos y ventas del negocio, mediante archivos csv; para persistirlo y poder trabjar con ellos
    """

    def __init__(self):
        self._productos = "productos.csv"
        self._ventas = "ventas.csv"
        self._inicializar_archivos()

    def _inicializar_archivos(self):
        """ Inicializamos los archivos csv donde se persistiran los datos"""
        if not os.path.exists(self._productos):
            pd.DataFrame(
                columns=[
                    "codigo_producto",
                    "nombre",
                    "categoria",                                        
                    "precio_venta",
                    "costo_unitario",
                    "stock_actual",
                ]
            ).to_csv(self._productos, index=False)
 
        if not os.path.exists(self._ventas):
            pd.DataFrame(
                columns=[
                    "codigo_venta", 
                    "codigo_producto", 
                    "cantidad", 
                    "precio_unitario",  
                    "fecha_venta"
                ]
            ).to_csv(self._ventas, index=False)



    def registrar_producto(self, un_producto):
        # Agrega un nuevo producto al inventario.
        if not isinstance(un_producto, Producto):
            raise TypeError("Debe ser una instancia de Producto.")


        #leemos el csv y lo pasamos al dateframe
        df_productos = pd.read_csv(self._productos)
        #chequeaos que no exista el producto
        if  un_producto.get_codigo_producto() in df_productos["codigo_producto"].values:
            raise ValueError(f"Ya existe un producto con código {un_producto.get_codigo_producto()}.")

        nuevo_producto = pd.DataFrame([{
            "codigo_producto": un_producto.get_codigo_producto(),
            "nombre": un_producto.nombre,
            "categoria": un_producto.categoria,
            "costo_unitario": un_producto.get_costo_unitario(),
            "precio_venta": un_producto.get_precio_venta(),
            "stock_actual": un_producto.get_stock_actual(),
        }])

        df_productos = pd.concat([df_productos, nuevo_producto], ignore_index=True)
        df_productos.to_csv(self._productos, index=False)


    def listar_producto(self):
        #leemos e archivo de productos
        df_productos = pd.read_csv(self._productos)

        if df_productos.empty:
            print("\n El inventario está vacío. No hay productos registrados.")
            return

        print("\n" + "=" * 85)
        print("Listado de productos")
        print("=" * 85)

        # Usamos to_string(index=False) para que se vea como una tabla limpia
        print(df_productos.to_string(index=False))
        print("-" * 85)


    def registrar_venta(self, mi_venta):
        # Agrega un nuevo producto al inventario.
        if not isinstance(mi_venta, Venta):
            raise TypeError("Debe ser una instancia de Venta.")

        #leemos el csv y lo pasamos al dateframe
        df_ventas = pd.read_csv(self._ventas)
        
        nueva_venta = pd.DataFrame([{
            "codigo_venta": mi_venta.get_codigo_venta(),
            "codigo_producto": mi_venta.get_codigo_producto(),
            "cantidad": mi_venta.get_cantidad_vendida(),
            "precio_unitario": mi_venta.get_precio_unitario(),
            "fecha_venta": mi_venta.get_fecha_venta(),
        }])

        df_ventas = pd.concat([df_ventas, nueva_venta], ignore_index=True)
        df_ventas.to_csv(self._productos, index=False)



if __name__ == '__main__':
    mi_inventario =  Inventario()
    
    producto_detergente = Producto(100, "Detergente Ala", "LIMPIEZA", 1200.0, 8500.50, 1000)
    producto_lavavajillas = Producto(101, "Lava Vajillas", "LIMPIEZA", 22000, 15000.50 , 1000)
    producto_yerba = Producto(102, "Yerba", "ALMACEN", 4000.0, 1850.50, 1000)

    mi_inventario.registrar_producto(producto_detergente)
    mi_inventario.registrar_producto(producto_lavavajillas)
    mi_inventario.registrar_producto(producto_yerba)

    ventas = []
    ventas.append( Venta(101, 50, 1500.00, '10-05-2026'))
    ventas.append( Venta(102, 25, 2210.55, '10-06-2026'))
    ventas.append( Venta(103, 25, 7500.25, '05-05-2026'))
    ventas.append( Venta(101, 15, 1350.33, '12-05-2026'))
    ventas.append( Venta(101, 15, 3650.22, '07-06-2026'))
    
    for i, elem in enumerate(ventas):
        mi_inventario.registrar_venta(elem)

   