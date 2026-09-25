import numpy as np

# Configuración
rng = np.random.default_rng(seed=42)   # semilla para resultados reproducibles
meses = ["Mes 1", "Mes 2", "Mes 3"]
dias = 30

# Matriz de ventas: 3 filas (meses) x 30 columnas (días), valores entre 1000 y 10000
ventas = rng.integers(1000, 10001, size=(len(meses), dias))

# 1. Total de ventas de cada mes (sumar a lo largo de las columnas → axis=1)
total_por_mes = ventas.sum(axis=1)

# 2. Promedio de cada día considerando los 3 meses (promediar las filas → axis=0)
promedio_por_dia = ventas.mean(axis=0)
mejor_dia = promedio_por_dia.argmax() + 1   # +1 porque los índices empiezan en 0

# 3. Mes con mayores ventas totales
mejor_mes = total_por_mes.argmax()

# Resultados
print("Matriz de ventas (forma):", ventas.shape)
print("\nTotal de ventas por mes:")
for mes, total in zip(meses, total_por_mes):
    print(f"  {mes}: ${total:,}")

print(f"\nDía con mejor promedio de ventas: día {mejor_dia} "
      f"(promedio ${promedio_por_dia.max():,.2f})")
print(f"Mes con más ventas: {meses[mejor_mes]} (${total_por_mes[mejor_mes]:,})")