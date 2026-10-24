# Sistema de Gestión de Inventario con Predicción de Ventas

**Materia**: Programación para Inteligencia Artificial
**Fecha**: 2026-10-19

## Estructura del proyecto (modularización por POO)

```
sistema_inventario/
├── main.py           # Punto de entrada
├── menu.py           # Clase MenuInteractivo (interfaz CLI)
├── inventario.py     # Clase Inventario (gestión + análisis con Pandas)
├── producto.py       # Clase Producto (modelo del artículo)
├── venta.py          # Clase Venta (modelo de la transacción)
├── predictor.py      # Clase PredictorVentas (ML con Scikit-learn)
├── test_sistema.py   # Script de pruebas automatizadas
└── README.md
```

## Ejecución

```bash
# Modo interactivo (menú)
python main.py

# Script de pruebas automatizadas (3 casos)
python test_sistema.py
```

## Dependencias

```bash
pip install numpy pandas scikit-learn
```

## Diseño orientado a objetos

- **`Producto`**: encapsula los datos del artículo (atributos privados con prefijo `_`, acceso vía `@property`). Expone métodos de negocio como `ganancia_unitaria()`, `margen_porcentaje()`, `aumentar_stock()` y `disminuir_stock()`.
- **`Venta`**: representa una transacción individual, con validación de cantidades y precios. Calcula el `total()` de la operación.
- **`Inventario`**: colección de productos y ventas. Centraliza el registro, descuenta stock automáticamente al vender, persiste todo en JSON y convierte el historial en un `DataFrame` de Pandas para análisis estadístico.
- **`PredictorVentas`**: entrena un modelo de regresión lineal **por producto** usando Scikit-learn. Aplica `StandardScaler` para normalización, `train_test_split` para separar datos, y expone métricas (MAE, RMSE, R²).
- **`MenuInteractivo`**: orquesta la UI por consola, coordinando las demás clases sin que ellas conozcan a la interfaz.

## Integración de bibliotecas de IA

- **NumPy**: cálculos vectorizados sobre predicciones, desviación estándar y manejo de arrays de features.
- **Pandas**: `DataFrame` del historial de ventas, agrupamientos por producto y por mes (`groupby`, `to_period`), estadísticas descriptivas.
- **Scikit-learn**:
  - `LinearRegression` como modelo base.
  - `StandardScaler` para normalizar la variable temporal.
  - `train_test_split` para dividir datos (75% entrenamiento / 25% prueba).
  - `mean_absolute_error`, `mean_squared_error`, `r2_score` como métricas.
