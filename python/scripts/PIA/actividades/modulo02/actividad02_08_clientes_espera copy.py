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

def crear_cliente(apellido, nombre, dni):
    return {
        "apellido": apellido,
        "nombre": nombre,
        "dni": dni,
                        
    }

def crear_ventanilla(nombre, duracion):
    return {
        "duracion_atencion": duracion, #maximo en minutos que puede ser atendido un cliente
        "nombre_ventanilla": nombre,
        "cliente": None,
        "tiempo_inicial": None
    }

def asignar_cliente(ventanilla, cliente):
    ventanilla["cliente"] = cliente
    ventanilla["tiempo_inicial"] = "20:10" # aca podemos usar funciones de timepo


clientes_espera = crear_cola()
cliente3 = crear_cliente("Sanchez","Ana Santa","32698457")
cliente4 = crear_cliente("Mortada","Carolina","15951951")
cliente5 = crear_cliente("Lucia","lucis","35654654")

enqueue(clientes_espera,  crear_cliente("Ruiz","Miguel", 35655458))
enqueue(clientes_espera, crear_cliente("Alvarez","Esteban", 55412245))
enqueue(clientes_espera, crear_cliente("Sanchez","Ana Santa", 32698457))
enqueue(clientes_espera, crear_cliente("Mortada","Carolina", 15951951))
enqueue(clientes_espera, crear_cliente("Lucia","lucis", 35654654))

enqueue(clientes_espera, crear_cliente("Hernandorte","ignacio",132987411))
enqueue(clientes_espera, crear_cliente("Baez","Estefania",65122245))
enqueue(clientes_espera, crear_cliente("Fernandez","marta",25100655))
enqueue(clientes_espera, crear_cliente("Mortada","Tamara",32051410))
enqueue(clientes_espera, crear_cliente("HUgo","Port", 36514125))

print(f"Clientes en espra {clientes_espera}")

