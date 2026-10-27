import os

import numpy as np
import pandas as pd
from producto import Producto
from venta import Venta


class Inventario:
    """
    Administra productos y ventas del negocio, mediante archivos csv, y dataframe,
    para percistencias, trabajar con ellos con Panda, y predecir ventas con scikit-learn
    """

    def __init__(self, sobreescribir = False, nombre_file_productos = "productos.csv", nombre_file_ventas = "ventas.csv"):
        self._sobreescribir = sobreescribir
        self._archivo_productos = nombre_file_productos
        self._archivo_ventas = nombre_file_ventas
        self._df_productos = None
        self._df_ventas = None

                
        self._inicializar_archivos()

    def _inicializar_archivos(self):
        """ Inicializamos los archivos csv donde se persistiran los datos"""

        #si el archivo no existe o sobreescribir es True se crea el archivo cvs, con una estructura inicial de sus columnas
        if self._sobreescribir or not os.path.exists(self._archivo_productos):
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
       
        if self._sobreescribir or not os.path.exists(self._archivo_ventas):
            pd.DataFrame(
                columns=[
                    "codigo_venta", 
                    "codigo_producto", 
                    "cantidad", 
                    "precio_unitario",  
                    "costo_unitario",   
                    "fecha_venta"
                ]
            ).to_csv(self._archivo_ventas, index=False)

        self._df_productos = pd.read_csv(
            self._archivo_productos,
            dtype={"codigo_producto": int, "stock_actual": int},
        )

        self._df_ventas = pd.read_csv(
            self._archivo_ventas,
            dtype={"codigo_venta": int, "codigo_producto": int},
        )

    def get_ventas_df_frame(self):
        """ Retorna el dataframe de ventas """
        return self._df_ventas

    def get_productos_df_frame(self):
        """ Retorna el dataframe de productos """
        return self._df_productos
    
    def registrar_producto(self, un_producto):
        """ Da de alta un nuevo registro, almacenandolo en el archivo csv como en el dataframe de productos """
        if not isinstance(un_producto, Producto):
            raise TypeError("Debe ser una instancia de Producto.")

        # chequeamos que no exista el producto
        if  un_producto.get_codigo_producto() in self._df_productos["codigo_producto"].values:
            raise ValueError(f"Ya existe un producto con código {un_producto.get_codigo_producto()}.")

        nuevo_producto = pd.DataFrame([{
            "codigo_producto": un_producto.get_codigo_producto(),
            "nombre": un_producto.nombre,
            "categoria": un_producto.categoria,            
            "precio_venta": un_producto.get_precio_venta(),
            "costo_unitario": un_producto.get_costo_unitario(),
            "stock_actual": un_producto.get_stock_actual(),
        }])

        self._df_productos = pd.concat([self._df_productos, nuevo_producto], ignore_index=True)
        self._df_productos.to_csv(self._archivo_productos, index=False)


    def listar_productos(self):
        """ Lista el dataframe de productos del inventario, mostrando sus datos"""
        if self._df_productos.empty:
            print("\n El inventario está vacío. No hay productos registrados.")
            return

        print("\n" + "=" * 85)
        print("Listado de productos")
        print("=" * 85)

        # Usamos to_string(index=False) para que se vea como una tabla limpia
        print(self._df_productos.to_string(index=False))
        print("-" * 85)

    def obtener_producto(self, codigo_bsq):
        """ Dado un determinado codigo de producto, busca el mismo en el dataframe de productos y caso de exito devuelve un modelo de la clase Producto"""
        codigo_bsq = int(codigo_bsq)
        fila_producto = self._df_productos.loc[self._df_productos['codigo_producto'] == codigo_bsq]        
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
        """ Da de alta una nueva venta, la almacena en el archivo csv de ventas como en el dataframe. """
        
        if not isinstance(mi_venta, Venta):
            raise TypeError("Debe ser una instancia de Venta.")

        producto = self.obtener_producto(mi_venta.get_codigo_producto())
        if producto is None:
            raise ValueError("Producto inexistente.")
        # descontamos stock
        cantidad = mi_venta.get_cantidad_vendida()
        stock_actual = producto.get_stock_actual()
        
        if stock_actual < cantidad:
            raise ValueError(f"Stock insuficiente ({stock_actual} < {cantidad}).")

        producto.disminuir_stock_actual(cantidad)
        
        # Descontar stock en el DataFrame
        codigo_producto_venta = mi_venta.get_codigo_producto()
        self._df_productos.loc[
            self._df_productos["codigo_producto"] == codigo_producto_venta,
            "stock_actual"
        ] -= cantidad
        self._df_productos.to_csv(self._archivo_productos, index=False)


        nueva_venta = pd.DataFrame([{
            "codigo_venta": mi_venta.get_codigo_venta(),
            "codigo_producto": mi_venta.get_codigo_producto(),
            "cantidad": mi_venta.get_cantidad_vendida(),
            "precio_unitario": mi_venta.get_precio_unitario(),
            "costo_unitario": mi_venta.get_costo_unitario(),
            "fecha_venta": mi_venta.get_fecha_venta(),
        }])

        self._df_ventas = pd.concat([self._df_ventas, nueva_venta], ignore_index=True)
        self._df_ventas.to_csv(self._archivo_ventas, index=False)

    def obtener_codigo_proxima_venta(self):
        """ Retorna el proximo codigo de venta (asumimos que es numerico y consecutivo) """        
        if self._df_ventas.empty or self._df_ventas['codigo_venta'].dropna().empty:
            proximo_codigo_venta = 1  # Primer ID si no hay registros
        else:
            proximo_codigo_venta = int(self._df_ventas['codigo_venta'].max() + 1)
        return proximo_codigo_venta

    def listar_ventas_historicas(self):
        """ Lista el dataframe de Ventas del inventario, mostrando sus datos"""
        if self._df_ventas.empty:
            print("\n El inventario está vacío. No hay ventas registradas.")
            return

        print("\n" + "=" * 85)
        print("Listado de Ventas")
        print("=" * 85)

        # Usamos to_string(index=False) para que se vea como una tabla limpia
        print(self._df_ventas.to_string(index=False))
        print("-" * 85)    


    def analizar_datos_historicos(self):
        """
        Realiza un análisis estadístico de las ventas usando Pandas y NumPy.
        Devuelve un diccionario con las métricas principales.
        """
        if self._df_ventas.empty:
            return {"mensaje": "No hay ventas registradas para analizar."}

        # Trabajamos sobre una copia para no ensuciar el DataFrame original
        df = self._df_ventas.copy()

        df["fecha_venta"] = pd.to_datetime(df["fecha_venta"], format="%d-%m-%Y") #convertimos a fecha sino explota
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

        analisis = {           
            "facturacion_total":          float(df["total"].sum()),
            "ticket_promedio":            float(df["total"].mean()),
            "ticket_mediano":             float(df["total"].median()),
            "desviacion_estandar_ticket": float(np.std(df["total"], ddof=0)),
            "fecha_primera_venta":        df["fecha_venta"].min().strftime("%Y-%m-%d"),
            "fecha_ultima_venta":         df["fecha_venta"].max().strftime("%Y-%m-%d"),
            "total_ventas_registradas": int(len(df)),
            "total_unidades_vendidas":  int(df["cantidad"].sum()),
            "ventas_por_producto": ventas_por_producto
        }
        return analisis


if __name__ == '__main__':
    mi_inventario =  Inventario(True, "prueba_productos.csv", "prueba_ventas.csv")
    mi_inventario.listar_productos()
    # mi_inventario.listar_ventas_historicas()

    print("Cargando nuevos productos")
    producto_detergente = Producto(100000, "Detergente Ala", "LIMPIEZA", 1200.0, 8500.50, 1000)
    producto_lavavajillas = Producto(100001, "Lava Vajillas", "LIMPIEZA", 22000, 15000.50 , 1000)
    producto_yerba = Producto(100002, "Yerba", "ALMACEN", 4000.0, 1850.50, 1000)

   

    mi_inventario.registrar_producto(producto_detergente)
    mi_inventario.registrar_producto(producto_lavavajillas)
    mi_inventario.registrar_producto(producto_yerba)
    mi_inventario.listar_productos()
