import pandas as pd
import numpy as np

"""
lista = [1, 2, 3, 4, 5]
array = np.array(lista)
print(array)
matriz = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(matriz)

ceros = np.zeros((3, 4))
unos = np.ones((2, 3))
rango = np.arange(0, 10, 2)
lineal = np.linspace(0, 1, 5)


print(ceros)
print(unos)
print(rango)
print(lineal)
print(f"Forma del vector: {array.shape}") #dimensoin del array
print(f"Forma de la matriz: {matriz.shape}") #dimensoin del array
print(f"Dimensiones del vector: {array.ndim}")
print(f"Total de elementos: {array.size}")
print(f"Tipo de datos: {array.dtype}")
"""

"""
array = np.array([10, 20, 30, 40, 50])
matriz = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(array[0])
print(matriz[1, 2])
print(matriz[0:2, 1:3])
print(matriz[1, :])
print(matriz[:, 1])
"""

"""
a = np.array([1, 2, 3, 4])
b = np.array([10, 20, 30, 40])
print(a + b)
print(a * b)
print(b / a)
print(a ** 2)
print(a + 10)
"""

"""
datos = np.array([12, 15, 18, 22, 25, 30, 35])
media = np.mean(datos)
mediana = np.median(datos)
desviacion = np.std(datos)
maximo = np.max(datos)
minimo = np.min(datos)
suma = np.sum(datos)
print(f"Media: {media}")
print(f"Mediana: {mediana}")
print(f"Desviación estándar: {desviacion}")
print(f"Máximo: {maximo}")
print(f"Mínimo: {minimo}")
print(f"Suma: {suma}")
"""

"""
array = np.arange(12)
print(f"vector es {array}")
matriz = array.reshape(3, 4)
print(matriz)
"""

"""
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(np.vstack([a, b]))
print(np.hstack([a, b]))
"""


notas = np.array([[85, 90, 78], [92, 88, 95], [78, 85, 82]])
print("Notas originales:")
print(notas)
bonus = np.array([5, 3, 2])
notas_con_bonus = notas + bonus
print("\nNotas con bonus:")
print(notas_con_bonus)


temperaturas_celsius = np.array([[20, 22, 19], [25, 28, 24], [18, 21, 20]])
temperaturas_fahrenheit = temperaturas_celsius * 9/5 + 32
print(temperaturas_fahrenheit)

"""
ingresos = np.array([50, 65, 45, 70, 55, 80, 60, 75, 52, 68])
media = np.mean(ingresos)
print(f"Media: {media}")

desviacion = np.std(ingresos)
ingresos_normalizados = (ingresos - media) / desviacion
print(f"Media normalizada: {np.mean(ingresos_normalizados):.10f}")
print(f"Desviación normalizada: {np.std(ingresos_normalizados):.2f}")



serie = pd.Series([10, 20, 30, 40, 50], index=['a', 'b', 'c', 'd', 'e'])
print(serie)
print(serie['a'])
print(serie.mean())

"""

"""
datos = { 'nombre': ['Ana', 'Carlos', 'Beatriz', 'Diego'], 'edad': [22, 25, 23, 24], 'ciudad': ['Buenos Aires', 'Córdoba', 'Rosario', 'Mendoza'] }
df = pd.DataFrame(datos)
"""
"""

print(df)

print(df.head())
print(f"Primeras filas {df.head(2)}")
print(f"Ultimas filas {df.tail(1)}")
print(df.info())
print(df.describe())

print(f"Los nombr son {df['nombre']}")
print(f"nombre y edad son {df[['nombre', 'edad']]}")
print(df.iloc[0])
print(df.loc[0, 'edad'])

mayores_23 = df[df['edad'] > 23]
print(mayores_23)
"""