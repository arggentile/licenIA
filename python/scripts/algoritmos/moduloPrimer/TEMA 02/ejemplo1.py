# Dataset simple: cada instancia tiene [edad, ingresos, etiqueta]
dataset = [
    [22, 35000, 0],
    [45, 82000, 1],
    [36, 62000, 1],
]

print("Cantidad de instancias:", len(dataset))
print("Primera instancia:", dataset[0])

# Acceso a un atributo (edad) de cada instancia
edades = [fila[0] for fila in dataset]
print("Edades:", edades)

