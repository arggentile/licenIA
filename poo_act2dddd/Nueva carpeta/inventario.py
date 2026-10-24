"""
Módulo: inventario.py
Descripción: Define la clase Inventario, que administra la colección de
productos y ventas. Centraliza el registro, la consulta y el análisis
histórico usando Pandas y NumPy.
"""

import json
import os
import numpy as np
import pandas as pd

from producto import Producto
from venta import Venta


class Inventario:
    """
    Administra productos y ventas del negocio.

    Atributos:
        _productos (dict): Diccionario {codigo: Producto}.
        _ventas (list): Lista de objetos Venta registrados.
        _archivo_datos (str): Ruta para persistir los datos.
    """

    def __init__(self, archivo_datos="datos_inventario.json"):
        self._productos = {}
        self._ventas = []
        self._archivo_datos = archivo_datos
        self._cargar_datos()

    # ------------------- Gestión de productos ------------------- #
    def registrar_producto(self, producto):
        """Agrega un nuevo producto al inventario."""
        if not isinstance(producto, Producto):
            raise TypeError("Debe ser una instancia de Producto.")
        if producto.codigo in self._productos:
            raise ValueError(f"Ya existe un producto con código {producto.codigo}.")
        self._productos[producto.codigo] = producto
        self._guardar_datos()

    def obtener_producto(self, codigo):
        """Devuelve el Producto correspondiente al código dado."""
        codigo = str(codigo).strip().upper()
        return self._productos.get(codigo)

    def listar_productos(self):
        """Devuelve una lista con todos los productos."""
        return list(self._productos.values())

    # ------------------- Gestión de ventas ------------------- #
    def registrar_venta(self, venta):
        """
        Registra una venta y actualiza automáticamente el stock del producto.
        """
        if not isinstance(venta, Venta):
            raise TypeError("Debe ser una instancia de Venta.")
        producto = self.obtener_producto(venta.codigo_producto)
        if producto is None:
            raise ValueError(f"No existe un producto con código {venta.codigo_producto}.")
        # Descuenta stock (puede lanzar error por stock insuficiente)
        producto.disminuir_stock(venta.cantidad)
        self._ventas.append(venta)
        self._guardar_datos()

    def listar_ventas(self):
        return list(self._ventas)

    # ------------------- Análisis con Pandas ------------------- #
    def ventas_a_dataframe(self):
        """
        Convierte el historial de ventas a un DataFrame de Pandas.
        Devuelve DataFrame vacío si aún no hay ventas registradas.
        """
        if not self._ventas:
            return pd.DataFrame(columns=["fecha", "codigo_producto",
                                        "cantidad", "precio_unitario", "total"])
        registros = [v.to_dict() for v in self._ventas]
        df = pd.DataFrame(registros)
        df["fecha"] = pd.to_datetime(df["fecha"])
        return df

    def analizar_historial(self):
        """
        Realiza un análisis estadístico de las ventas usando Pandas y NumPy.
        Devuelve un diccionario con las métricas principales.
        """
        df = self.ventas_a_dataframe()
        if df.empty:
            return {"mensaje": "No hay ventas registradas para analizar."}

        resumen = {
            "total_ventas_registradas": len(df),
            "total_unidades_vendidas": int(df["cantidad"].sum()),
            "facturacion_total": float(df["total"].sum()),
            "ticket_promedio": float(df["total"].mean()),
            "ticket_mediano": float(df["total"].median()),
            "desviacion_estandar_ticket": float(np.std(df["total"])),
            "fecha_primera_venta": df["fecha"].min().strftime("%Y-%m-%d"),
            "fecha_ultima_venta": df["fecha"].max().strftime("%Y-%m-%d"),
        }

        # Ventas agrupadas por producto
        ventas_por_producto = (
            df.groupby("codigo_producto")
              .agg(unidades=("cantidad", "sum"),
                   facturacion=("total", "sum"),
                   ticket_promedio=("total", "mean"))
              .sort_values("facturacion", ascending=False)
        )
        resumen["ventas_por_producto"] = ventas_por_producto

        # Ventas por mes
        df["mes"] = df["fecha"].dt.to_period("M")
        ventas_por_mes = (
            df.groupby("mes")
              .agg(unidades=("cantidad", "sum"),
                   facturacion=("total", "sum"))
        )
        resumen["ventas_por_mes"] = ventas_por_mes

        return resumen

    # ------------------- Persistencia en JSON ------------------- #
    def _guardar_datos(self):
        """Persiste productos y ventas en un archivo JSON."""
        datos = {
            "productos": [p.to_dict() for p in self._productos.values()],
            "ventas": [v.to_dict() for v in self._ventas],
        }
        try:
            with open(self._archivo_datos, "w", encoding="utf-8") as f:
                json.dump(datos, f, indent=2, ensure_ascii=False)
        except IOError as e:
            print(f"[Advertencia] No se pudo guardar: {e}")

    def _cargar_datos(self):
        """Carga productos y ventas desde el archivo JSON si existe."""
        if not os.path.exists(self._archivo_datos):
            return
        try:
            with open(self._archivo_datos, "r", encoding="utf-8") as f:
                datos = json.load(f)
            for p in datos.get("productos", []):
                producto = Producto(
                    codigo=p["codigo"],
                    nombre=p["nombre"],
                    precio_venta=p["precio_venta"],
                    costo=p["costo"],
                    stock_actual=p["stock_actual"],
                    categoria=p.get("categoria", "General"),
                )
                self._productos[producto.codigo] = producto
            for v in datos.get("ventas", []):
                venta = Venta(
                    codigo_producto=v["codigo_producto"],
                    cantidad=v["cantidad"],
                    precio_unitario=v["precio_unitario"],
                    fecha=v["fecha"],
                )
                self._ventas.append(venta)
        except (IOError, json.JSONDecodeError) as e:
            print(f"[Advertencia] No se pudieron cargar los datos: {e}")
