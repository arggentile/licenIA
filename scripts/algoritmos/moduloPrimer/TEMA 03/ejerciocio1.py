import csv
with open("entradasSS.csv", mode="r", newline="", encoding="utf-8") as archivo:
    lector = csv.reader(archivo)
    encabezado = next(lector)
    filas = list(lector)

print("Encabezado:", encabezado)
print("Primera fila:", filas[0])
print("Cantidad de registros:", len(filas))
