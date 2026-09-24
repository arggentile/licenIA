import pandas as pd

datos = {
    "edad": [22, 45, 36],
    "ingresos": [35000, 82000, 62000],
    "etiqueta": [0, 1, 1]
}

df = pd.DataFrame(datos)

print(df)
print("Columnas:", df.columns)
print("Cantidad de filas:", len(df))
