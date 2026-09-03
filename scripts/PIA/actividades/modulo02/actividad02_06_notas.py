""" Funciones para manejar una cola (FIFO) """
def crear_cola():
    return []

def esta_vacia(cola):
    return len(cola) == 0

def enqueue(cola, elemento):
    cola.append(elemento)  # agrega al final

def dequeue(cola):
    if not esta_vacia(cola):
        return cola.pop(0)  # saca del principio
    return None

def tamanio(cola):
    return len(cola)


def crear_notero():
    return {
        "notas": crear_cola(),
        "capacidad": 5 #puede modificarse en un futuro
    }


def agregar_calificacion(notero, nota):
    # Si está llena, saco la más antigua antes de agregar
    if tamanio(notero["notas"]) >= notero["capacidad"]:
        eliminada = dequeue(notero["notas"])
        print(f"  Cola llena → se elimina la nota más antigua: {eliminada}")
    
    enqueue(notero["notas"], nota) # agregamos nueva nota

    
def calcular_promedio(notas):
    promedio = sum(notas) / tamanio(notas)
    return promedio



# Simulación
notero = crear_notero()
notas = [10, 7, 9.5, 9.3, 5.8, 7.5, 9, 7, 10]

for n in notas:
    agregar_calificacion(notero, n)

print(f"las notas son: {notero['notas']}")    
print(f"El promedio de las notas es de : {calcular_promedio(notero["notas"])}")    

nuevas_notas = [7, 8, 8, 9.4]
for n in notas:
    agregar_calificacion(notero, n)
    print(f"las notas son: {notero['notas']}")    
    print(f"El promedio de las notas es de : {calcular_promedio(notero["notas"])}")    
