"""
estudiantes = ['Ana', 'Carlos']
estudiantes.append('María')
print(estudiantes) # [‘Ana’, ‘Carlos’, ‘María’]     
estudiantes.insert(1, 'julina')
print(estudiantes) # [‘Ana’, ‘Carlos’, ‘María’]     
estudiantes.append('Carlos')
print(estudiantes) # [‘Ana’, ‘Carlos’, ‘María’]     

v = estudiantes.pop(2)  # [‘Ana’, ‘Carlos’, ‘María’]     
print(estudiantes) # [‘Ana’, ‘Carlos’, ‘María’]     

numeros = [15, 8, 23, 4, 16, 42, 11]
print(len(numeros)) # 7 (cantidad de elementos)
print(sum(numeros)) # 119 (suma de todos los elementos)
print(min(numeros)) # 4 (elemento más pequeño)
print(max(numeros)) # 42 (elemento más grande)

frutas = ['manzana', 'banana', 'naranja']
for indice, fruta in enumerate(frutas):
    print(f"Posición {indice}: {fruta}")

# Dataset de ejemplo: [edad, altura_cm, peso_kg]
datos = [
[25, 175, 70],
[30, 180, 85],
[22, 165, 60],
[35, 178, 80],
[28, 172, 75]
]
# Extraer solo las edades
edades = [persona[0] for persona in datos]
print("Edades:", edades)
altura = [persona[1] for persona in datos]
print("Altura:", altura)
# Calcular estadísticas
edad_promedio = sum(edades) / len(edades)
edad_minima = min(edades)
edad_maxima = max(edades)
print(f"Edad promedio: {edad_promedio}")
print(f"Edad mínima: {edad_minima}")
print(f"Edad máxima: {edad_maxima}")
# Filtrar personas mayores de 25 años
mayores_25 = [persona for persona in datos if persona[0] > 25]
print(f"Personas mayores de 25: {len(mayores_25)}")    

estudiante = {
"nombre": "Ana",
"edad": 20,
"carrera": "Lic. en Inteligencia Artificial",
"promedio": 8.5
}
print(estudiante["nombre"]) # Ana
print(estudiante["promedio"]) # 8.5

estudiante["email"] = "ana@ejemplo.com"
estudiante["edad"] = 21
print(estudiante)

print(estudiante.keys()) # dict_keys([‘nombre’, ‘edad’, ‘carrera’, ‘promedio’])
print(estudiante.values()) # dict_values([‘Ana’, 21, ‘Inteligencia Artificial’, 8.5])
print(estudiante.items()) # dict_items([(‘nombre’, ‘Ana’), ...])



def contar_palabras(texto):
    palabras = texto.lower().split()
    frecuencias = {}
    for palabra in palabras:
        if palabra in frecuencias:
            frecuencias[palabra] += 1
        else:
            frecuencias[palabra] = 1
    return frecuencias

texto = "python es genial python es poderoso python es versátil"
frecuencias = contar_palabras(texto)
print(frecuencias)
# {‘python’: 3, ‘es’: 3, ‘genial’: 1, ‘poderoso’: 1, ‘versátil’: 1}
"""


estudiantes = [
{"nombre": "Ana", "edad": 20, "promedio": 8.5},
{"nombre": "Carlos", "edad": 22, "promedio": 7.0},
{"nombre": "Beatriz", "edad": 21, "promedio": 9.0}
]

# Encontrar estudiantes con promedio mayor a 8
destacados = [est for est in estudiantes if est["promedio"] >= 8.0]

for estudiante in destacados:
    print(f"{estudiante['nombre']}: {estudiante['promedio']}")