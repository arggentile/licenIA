



    

    def predecir_total(self, codigo_producto, dias_adelante=7):
        """Devuelve el total estimado de unidades a vender en el periodo."""
        predicciones = self.predecir(codigo_producto, dias_adelante)
        if predicciones is None:
            return None
        return float(np.sum(predicciones))

    # ------------------- Consultas ------------------- #
    def obtener_metricas(self, codigo_producto):
        """Devuelve las métricas del modelo entrenado para un producto."""
        codigo_producto = codigo_producto.strip().upper()
        if codigo_producto not in self._modelos:
            return None
        return self._modelos[codigo_producto][2]

    def productos_entrenados(self):
        return list(self._modelos.keys())
