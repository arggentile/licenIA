import csv

datos = [
    ["edad", "ingresos", "etiqueta"],
    [22, 35000, 0],
    [45, 82000, 1],
    [36, 62000, 1],
    ["edad", "ingresos", "etiqueta"],
    [22, 35000, 0],
    [45, 82000, 1],
    [36, 62000, 1]

]

with open("salida.csv", mode="w", newline="", encoding="utf-8") as archivo:
    escritor = csv.writer(archivo)
    escritor.writerows(datos)

print("Archivo CSV generado correctamente.")
