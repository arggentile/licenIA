import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

class Predicciones:
    """
    Entrena un modelo de regresión lineal por producto para predecir
    cantidades vendidas en función del tiempo.

    Atributos:
        _modelos (dict): {codigo_producto: (modelo, scaler, metricas)}.
    """

    # ------------------- Entrenamiento ------------------- #
    def entrenar_modelo_producto(self, codigo_producto, df_ventas):
        """
        Entrena un modelo de regresión lineal para un producto puntual.

        El eje X es el número de día desde la primera venta registrada
        y el eje Y es la cantidad vendida en esa fecha.
        """

        #trabajamos con una copia del dataframe
        datos = df_ventas[df_ventas["codigo_producto"] == codigo_producto].copy()

     
        # Agrupamos ventas por fecha para obtener la demanda diaria
        datos = (datos.groupby("fecha")
                       .agg(cantidad=("cantidad", "sum"))
                       .reset_index()
                       .sort_values("fecha"))

        fecha_base = datos["fecha"].min()
        datos["dia"] = (datos["fecha"] - fecha_base).dt.days

        X = datos[["dia"]].values
        y = datos["cantidad"].values

        # División en entrenamiento y prueba
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.3, random_state=42
        )

        # Normalización de la variable independiente
        scaler = StandardScaler()
        X_train_norm = scaler.fit_transform(X_train)
        X_test_norm = scaler.transform(X_test)

        # Entrenamiento
        modelo = LinearRegression()
        modelo.fit(X_train_norm, y_train)

        # Evaluación
        y_pred = modelo.predict(X_test_norm)
        metricas = {
            "mae": float(mean_absolute_error(y_test, y_pred)),
            "rmse": float(np.sqrt(mean_squared_error(y_test, y_pred))),
            "r2": float(r2_score(y_test, y_pred)) if len(y_test) > 1 else None,
            "coeficiente": float(modelo.coef_[0]),
            "intercepto": float(modelo.intercept_),
            "tamanio_muestras_entrenamiento": len(X_train),
            "tamanio_muestras_prueba": len(X_test),
            "fecha_base": fecha_base.strftime("%Y-%m-%d"),
            "ultimo_dia": int(datos["dia"].max()),
        }

        self._modelos[codigo_producto] = (modelo, scaler, metricas)
        return {
            "codigo": codigo_producto,
            "exito": True,
            "metricas": metricas,
        }

    def predecir_ventas_futuras(self, codigo_producto, dias_adelante=7):
        """
        Predice la cantidad de ventas diarias para los próximos `dias_adelante`
        días a partir del último registro de entrenamiento.
        """
        codigo_producto = codigo_producto.strip().upper()
        if codigo_producto not in self._modelos:
            return None

        modelo, scaler, metricas = self._modelos[codigo_producto]
        ultimo_dia = metricas["ultimo_dia"]

        dias_futuros = np.array(
            [[ultimo_dia + i] for i in range(1, dias_adelante + 1)]
        )
        dias_futuros_norm = scaler.transform(dias_futuros)
        predicciones = modelo.predict(dias_futuros_norm)

        # Las ventas no pueden ser negativas: aplicamos piso en 0
        predicciones = np.maximum(predicciones, 0)
        return predicciones

    def productos_entrenados(self):
        return list(self._modelos.keys())
    