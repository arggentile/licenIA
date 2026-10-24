import os

import numpy as np
import pandas as pd

from producto import Producto
from venta import Venta


class Inventario:
    """
    Administra productos y ventas del negocio, mediante archivos csv; 
    para persistencias, trabjar con ellos con pANDA, y precir ventas con skir-leranig
    """

    def __init__(self, nombre_file_productos = "productos.csv", nombre_file_ventas = "ventas.csv"):
        self._archivo_productos = nombre_file_productos
        self._archivo_ventas = nombre_file_ventas
        self._df_productos = None
        self._df_ventas = None
                
        self._inicializar_archivos()

    def _inicializar_archivos(self):
        """ Inicializamos los archivos csv donde se persistiran los datos"""
        if not os.path.exists(self._archivo_productos):
            pd.DataFrame(
                columns=[
                    "codigo_producto",
                    "nombre",
                    "categoria",                                        
                    "precio_venta",
                    "costo_unitario",
                    "stock_actual",
                ]
            ).to_csv(self._archivo_productos, index=False)
       
        if not os.path.exists(self._archivo_ventas):
            pd.DataFrame(
                columns=[
                    "codigo_venta", 
                    "codigo_producto", 
                    "cantidad", 
                    "precio_unitario",  
                    "fecha_venta"
                ]
            ).to_csv(self._archivo_ventas, index=False)

        self.df_productos = pd.read_csv(
            self._archivo_productos,
            dtype={"codigo_producto": int, "stock_actual": int},
        )

        self.df_ventas = pd.read_csv(
            self._archivo_ventas,
            dtype={"codigo_venta": int, "codigo_producto": int},
        )

    def registrar_producto(self, un_producto):
        # Agrega un nuevo producto al inventario.
        if not isinstance(un_producto, Producto):
            raise TypeError("Debe ser una instancia de Producto.")

        #chequeamos que no exista el producto
        if  un_producto.get_codigo_producto() in self.df_productos["codigo_producto"].values:
            raise ValueError(f"Ya existe un producto con código {un_producto.get_codigo_producto()}.")

        nuevo_producto = pd.DataFrame([{
            "codigo_producto": un_producto.get_codigo_producto(),
            "nombre": un_producto.nombre,
            "categoria": un_producto.categoria,
            "costo_unitario": un_producto.get_costo_unitario(),
            "precio_venta": un_producto.get_precio_venta(),
            "stock_actual": un_producto.get_stock_actual(),
        }])

        self.df_productos = pd.concat([self.df_productos, nuevo_producto], ignore_index=True)
        self.df_productos.to_csv(self._archivo_productos, index=False)


    def listar_productos(self):
        if self.df_productos.empty:
            print("\n El inventario está vacío. No hay productos registrados.")
            return

        print("\n" + "=" * 85)
        print("Listado de productos")
        print("=" * 85)

        # Usamos to_string(index=False) para que se vea como una tabla limpia
        print(self.df_productos.to_string(index=False))
        print("-" * 85)

    def obtener_producto(self, codigo_bsq):
            codigo_bsq = int(codigo_bsq)
            fila_producto = self.df_productos.loc[self.df_productos['codigo_producto'] == codigo_bsq]        
            if fila_producto.empty:
                return None
            fila_producto = fila_producto.iloc[0]  # Series con las columnas del producto
            return Producto(
                codigo_producto=int(fila_producto['codigo_producto']),
                nombre=fila_producto['nombre'],
                categoria=fila_producto['categoria'],
                precio_venta=float(fila_producto['precio_venta']),
                costo_unitario=float(fila_producto['costo_unitario']),
                stock_actual=int(fila_producto['stock_actual']),
            )


    def registrar_venta(self, mi_venta):
        # Agrega un nuevo producto al inventario.
        if not isinstance(mi_venta, Venta):
            raise TypeError("Debe ser una instancia de Venta.")

        if not self.obtener_producto(mi_venta.get_codigo_producto()):
            raise TypeError("Codigo de producto inexistente.")
                    

        nueva_venta = pd.DataFrame([{
            "codigo_venta": mi_venta.get_codigo_venta(),
            "codigo_producto": mi_venta.get_codigo_producto(),
            "cantidad": mi_venta.get_cantidad_vendida(),
            "precio_unitario": mi_venta.get_precio_unitario(),
            "fecha_venta": mi_venta.get_fecha_venta(),
        }])

        self.df_ventas = pd.concat([self.df_ventas, nueva_venta], ignore_index=True)
        self.df_ventas.to_csv(self._archivo_ventas, index=False)

    def obtener_codigo_proxima_venta(self):
        
        if self.df_ventas.empty or self.df_ventas['codigo_venta'].dropna().empty:
            proximo_codigo_venta = 1  # Primer ID si no hay registros
        else:
            proximo_codigo_venta = int(self.df_ventas['codigo_venta'].max() + 1)
        return proximo_codigo_venta

    def listar_ventas_historicas(self):
   
        if self.df_ventas.empty:
            print("\n El inventario está vacío. No hay ventas registradas.")
            return

        print("\n" + "=" * 85)
        print("Listado de Ventas")
        print("=" * 85)

        # Usamos to_string(index=False) para que se vea como una tabla limpia
        print(self.df_ventas.to_string(index=False))
        print("-" * 85)    

    def analizar_datos_historicos(self):
        """
        Realiza un análisis estadístico de las ventas usando Pandas y NumPy.
        Devuelve un diccionario con las métricas principales.
        """
        print("\n--- Análisis de ventas históricas (Pandas) ---")

        if self.df_ventas.empty:
            return {"mensaje": "No hay ventas registradas para analizar."}

        # Trabajamos sobre una copia para no ensuciar el DataFrame original
        df = self.df_ventas.copy()

        # Calculamos el total de cada venta
        df["total"] = df["cantidad"] * df["precio_unitario"]

        # Ventas agrupadas por producto
        ventas_por_producto = (
            df.groupby("codigo_producto")
                .agg(unidades=("cantidad", "sum"),
                    facturacion=("total", "sum"),
                    ticket_promedio=("total", "mean"))
                .sort_values("facturacion", ascending=False)
        )        

        resumen = {
            

            "facturacion_total":          float(df["total"].sum()),
            "ticket_promedio":            float(df["total"].mean()),
            "ticket_mediano":             float(df["total"].median()),
            "desviacion_estandar_ticket": float(np.std(df["total"], ddof=0)),
            "fecha_primera_venta":        df["fecha_venta"].min().strftime("%Y-%m-%d"),
            "fecha_ultima_venta":         df["fecha_venta"].max().strftime("%Y-%m-%d"),
        }


       
        
        print(f"Total de Ventas registradas       : {len(df)}")
        print(f"Unidades totales vendidas: {int(df["cantidad"].sum())}")
        print(f"Facturación total        : ${float(df["total"].sum()):.2f}")
        print(f"Ticket promedio          : ${float(df["total"].mean()):.2f}")
        print(f"Ticket mediano           : ${float(df["total"].median()):.2f}")
        print(f"Desv. estándar ticket    : ${float(np.std(df["total"], ddof=0)):.2f}")
        print(f"Primera venta            : {resumen['fecha_primera_venta']}")
        print(f"Última venta             : {resumen['fecha_ultima_venta']}")

        print("\n>> Ventas por producto:")
        print(resumen["ventas_por_producto"].to_string())

        print("\n>> Ventas por mes:")
        print(resumen["ventas_por_mes"].to_string())


if __name__ == '__main__':
    mi_inventario =  Inventario("prueba_productos.csv", "prueba_ventas.csv")
    mi_inventario.listar_productos()
    mi_inventario.listar_ventas_historicas()

    print("Cargando nuevos productos")
    producto_detergente = Producto(10, "Detergente Ala", "LIMPIEZA", 1200.0, 8500.50, 1000)
    producto_lavavajillas = Producto(11, "Lava Vajillas", "LIMPIEZA", 22000, 15000.50 , 1000)
    producto_yerba = Producto(12, "Yerba", "ALMACEN", 4000.0, 1850.50, 1000)


    mi_inventario.registrar_producto(producto_detergente)
    mi_inventario.registrar_producto(producto_lavavajillas)
    mi_inventario.registrar_producto(producto_yerba)

    ventas = []
    ventas.append( Venta(5000, 10, 50, 1500.00, 1000,'10-05-2026'))
    ventas.append( Venta(5001, 11, 25, 2210.55, 2000,'10-06-2026'))
    ventas.append( Venta(5002, 10, 25, 7500.25, 700, '05-05-2026'))
    ventas.append( Venta(5003, 12, 15, 1350.33, 1200.00, '12-05-2026'))
    ventas.append( Venta(5004, 12, 15, 3650.22,  3000.00, '07-06-2026'))
    
    for i, elem in enumerate(ventas):
        mi_inventario.registrar_venta(elem)

   