

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



