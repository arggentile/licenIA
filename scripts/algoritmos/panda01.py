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
print(f"LAS edades son: {edades}")


#mostrar fila

primeras_filas = df[0:2]
print(primeras_filas)



df_filtrado = df[df["ingresos"] > 50000]

print(f"Edades filtradas: {df_filtrado}")

print(df)