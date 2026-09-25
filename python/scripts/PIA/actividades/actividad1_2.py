import numpy as np
import random

""" 

La normalización Min-Max transforma los valores numéricos de un conjunto de datos para que todos queden 
dentro de un rango fijo, comúnmente entre 0 y 1

min-max con la biblioteca NumPy en Python, debes restar el valor mínimo del arreglo 
y dividir el resultado entre la diferencia del valor máximo y el valor mínimo.
"""
grados_celsius = []
humedad = []
presion_pascales = []

for i in range(100):
    grados_celsius.append(random.randint(-30, 60))
    humedad.append(random.uniform(0, 100))
    presion_pascales.append(random.uniform(800, 1200))


datos = np.column_stack([grados_celsius, presion_pascales, humedad])

print(F"Data {datos}")


nombres = ["Temperatura", "Presión", "Humedad"]
print(f"{'Variable':<13}{'Mínimo':>13}{'Máximo':>13}{'Media':>13}{'Desv.':>13}")
for nombre, col in zip(nombres, datos.T):
    print(f"{nombre:<13}{col.min():>13.3f}{col.max():>13.3f}"
    f"{col.mean():>13.3f}{col.std():>13.3f}")
        

minimo = datos.min(axis=0)
maximo = datos.max(axis=0)
datos_minmax = (datos - minimo) / (maximo - minimo)
print(f"Minimo es: {minimo}")
print(f"Maxim es: {minimo}")
print(f"datos_minmax: {datos_minmax}")

print(f" \n \n ------------------------------ \n \n ")


media = np.mean(datos)
desviacion = np.std(datos)
ingresos_normalizados1 = (datos) / desviacion
print(f"Media normalizada: {np.mean(ingresos_normalizados1):.10f}")
print(f"Desviación normalizada: {np.std(ingresos_normalizados1):.2f}")
print(f"Nomrlizados: {ingresos_normalizados1}")




"""
La normalización Min-Max transforma los valores numéricos de un conjunto de datos
para que todos queden dentro de un rango fijo, comúnmente entre 0 y 1.
Fórmula: (x - mínimo) / (máximo - mínimo)

La estandarización transforma los datos para que tengan media 0 y desviación 1.
Fórmula: (x - media) / desviación
"""

# ---------- Generación de datos con NumPy (sin bucles) ----------
rng = np.random.default_rng()
n = 100

grados_celsius   = rng.integers(-30, 61, size=n)          # °C (61 para incluir el 60)
presion_pascales = rng.uniform(80000, 120000, size=n)     # Pa
humedad          = rng.uniform(0, 100, size=n)            # %

datos = np.column_stack([grados_celsius, presion_pascales, humedad])
nombres = ["Temperatura", "Presión", "Humedad"]

np.set_printoptions(precision=3, suppress=True)


def resumen(titulo, matriz):
    """Muestra mínimo, máximo, media y desviación de cada columna."""
    print(f"\n=== {titulo} ===")
    print(f"{'Variable':<13}{'Mínimo':>13}{'Máximo':>13}{'Media':>13}{'Desv.':>13}")
    for nombre, col in zip(nombres, matriz.T):
        print(f"{nombre:<13}{col.min():>13.3f}{col.max():>13.3f}"
              f"{col.mean():>13.3f}{col.std():>13.3f}")


print("Primeras 5 mediciones originales:\n", datos[:5])
resumen("Datos originales", datos)


# ---------- Método 1: Min-Max ----------
minimo = datos.min(axis=0)
maximo = datos.max(axis=0)
datos_minmax = (datos - minimo) / (maximo - minimo)

print(f"\nMínimo por variable: {minimo}")
print(f"Máximo por variable: {maximo}")
print("Primeras 5 mediciones Min-Max:\n", datos_minmax[:5])
resumen("Min-Max", datos_minmax)

print("¿Mínimos = 0?", np.allclose(datos_minmax.min(axis=0), 0))
print("¿Máximos = 1?", np.allclose(datos_minmax.max(axis=0), 1))

print("\n------------------------------")


# ---------- Método 2: Estandarización ----------
media = datos.mean(axis=0)          # una media por columna
desviacion = datos.std(axis=0)      # una desviación por columna
datos_std = (datos - media) / desviacion

print(f"\nMedia por variable: {media}")
print(f"Desviación por variable: {desviacion}")
print("Primeras 5 mediciones estandarizadas:\n", datos_std[:5])
resumen("Estandarización", datos_std)

print("¿Medias = 0?", np.allclose(datos_std.mean(axis=0), 0))
print("¿Desviaciones = 1?", np.allclose(datos_std.std(axis=0), 1))


# ---------- Comparación ----------
print("\n=== Comparación ===")
for i, nombre in enumerate(nombres):
    r_minmax = np.corrcoef(datos[:, i], datos_minmax[:, i])[0, 1]
    r_std = np.corrcoef(datos[:, i], datos_std[:, i])[0, 1]
    print(f"{nombre}: correlación con original → "
          f"Min-Max = {r_minmax:.3f}, Estandarización = {r_std:.3f}")
    