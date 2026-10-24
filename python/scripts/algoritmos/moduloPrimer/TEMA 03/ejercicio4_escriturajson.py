import json

instancias = [
    {"edad": 22, "ingresos": 35000, "etiqueta": 0},
    {"edad": 45, "ingresos": 82000, "etiqueta": 1}
]

with open("salidaSSS.json", "w", encoding="utf-8") as archivo:
    json.dump(instancias, archivo, indent=4)

print("Archivo JSON generado correctamente.")