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

def crear_sala_emergencia():
    return {
        "urgentes": crear_cola(),
        "no_urgentes":  crear_cola(),
    }

def agregar_paciente(sala, paciente, urgente = True):
    if(urgente==True):
        enqueue(sala['urgentes'], paciente)
    else:
        enqueue(sala['no_urgentes'], paciente)


def atender_paciente(sala):
    #priorizamos las urgencias
    if(tamanio(sala['urgentes'])>0):
        paciente = dequeue(sala['urgentes'])
        print(f"Atendiendo el paciuente {paciente}")
    elif(tamanio(sala['no_urgentes'])>0):  
        paciente = dequeue(sala['no_urgentes'])
        print(f"Atendiendo el paciuente {paciente}")  
    else:
        print(f"Sin pacientes para atender")

def es_sala_vacia(sala):
    return (tamanio(sala['urgentes']) == 0 and tamanio(sala['no_urgentes']) == 0)

                
sala_emergencia =   crear_sala_emergencia()
pacientes = [
    { 
        "nombre" : "Miguel",
        "urgente" : True,
                 
    },
    { 
        "nombre" : "Patricia",
        "urgente" : False,
                 
    },
    { 
        "nombre" : "luisa",
        "urgente" : False,
                 
    },
    { 
        "nombre" : "raul",
        "urgente" : True,
                 
    },
    { 
        "nombre" : "Esteban",
        "urgente" : False,
                 
    }
]

for pacnt in pacientes:
    agregar_paciente(sala_emergencia, pacnt["nombre"], pacnt["urgente"])

print(f" La lista de pacientes es:  {sala_emergencia}")

while(es_sala_vacia(sala_emergencia) ==  False):
    atender_paciente(sala_emergencia)
