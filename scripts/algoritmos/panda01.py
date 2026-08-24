import pandas as pd

datos = {
    "edad": [22, 45, 36],
    "ingresos": [35000, 82000, 62000],
    "etiqueta": [0, 1, 1]
}

df = pd.DataFrame(datos)

print(df)
print("Columnas:", df.columns)
# mustar solo columna edad
edades = df["edad"]
print(edades)

#mostrar fila
primeras_filas = df[0:2]
print(primeras_filas)

"""print("Columnas:", df.rows)

print("Cantidad de filas:", len(df))
print("Cantidad de filas:", df[0])

df_filtrado = df[df["ingresos"] > 50000]

print("Edades:")
print(edades)
print("\nInstancias filtradas:")
print(df_filtrado)
"""