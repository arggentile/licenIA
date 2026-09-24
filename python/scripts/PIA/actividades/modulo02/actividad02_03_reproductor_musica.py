def crear_cola():
    return []

def esta_vacia(cola):
    return len(cola) == 0

def enqueue(cola, elemento):
    cola.append(elemento)

def dequeue(cola):
    if not esta_vacia(cola):
        return cola.pop(0)
    return None

def ver_frente(cola):
    if not esta_vacia(cola):
        return cola[0]
    return None

def tamanio(cola):
    return len(cola)

def reproducir_cancion(reproductor):
    cancion_actual = dequeue(reproductor['canciones'])
    reproductor["cancion_actual"] = cancion_actual
    print(f"Cancion actual reproduciendose: {cancion_actual}")
    
def crear_reproductor():
    return {
        "canciones": crear_cola(),
        "cancion_actual":  None
    }

reproductor = crear_reproductor()
print(f" La lista de canciones es: {reproductor}")

canciones = ["Cancion A", "Cancion B", "Cancion C", "Cancion D", "Cancion E"]
for cancion in canciones:
    enqueue(reproductor['canciones'], cancion)
print(f" La lista de canciones es: {reproductor}")

while(tamanio(reproductor['canciones'])):
    reproducir_cancion(reproductor)
    print(f"Quedan en la lista un total de : {tamanio(reproductor['canciones'])}")
