import json

with open("data.json", "r", encoding="utf-8") as archivo:
    datos = json.load(archivo)

print("Cantidad de instancias:", len(datos))
print("Primera instancia:", datos[0])

