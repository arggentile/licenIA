""" INCIO DE FUNCIONALIDAD PARA COLAS """
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
""" INCIO DE FUNCIONALIDAD PARA COLAS """

""" INCIO DE FUNCIONALIDAD estudiantes """

# Comprueba si el nro de legajo existe en la lista de estudiante
def existe_legajo(lista_estudiantes, legajo):
    for estudiante in lista_estudiantes:
        if estudiante["legajo"] == legajo:
            return True
    return False

# Busca si existe un estudiante (pasando su nro de legajo) en la lista.
# Si existe devuelve su posicion en la lista caso contrario None
def buscar_x_legajo(lista_estudiantes, legajo):
    for indice, estudiante in enumerate(lista_estudiantes):
        if estudiante["legajo"] == legajo:
            return indice
    return None

# verifica que una nota este en el rango entre 0 y 10, devulve valor logico de acuerdo ai cumple la condicion.
def nota_valida(nota):
    if(nota>0 and nota<=10):
        return True
    return False

# crea un estudiante, con nombre, legajo, calificaciones y promedio
def crear_estudiante(nombre, legajo):
    return {
        "nombre": nombre,
        "legajo": legajo,
        "calificaciones": [],
        "promedio": 0.0 #por defecto se coloca en 0
    }

def ordenar_estudiantes_por_promedio(lista_estudiantes):
    n = len(lista_estudiantes)
    for i in range(n - 1):
        #agarro el primero y lo compara que el resto, despues el segundo y asi sucesivamente, se van comparando pares de hermano
        for j in range(n - 1 - i):
            # Compra hermanos y los rotas transladando el menor hacia el fondo, 
            if lista_estudiantes[j]["promedio"] > lista_estudiantes[j + 1]["promedio"]:
                temporal = lista_estudiantes[j]
                lista_estudiantes[j] = lista_estudiantes[j + 1]
                lista_estudiantes[j + 1] = temporal        


def mostrar_estudiante(lista_estudiantes):
    ordenar_estudiantes_por_promedio(lista_estudiantes)
    for estudiante in lista_estudiantes:
        print(f"Legajo: {estudiante['legajo']}, Nombre: {estudiante['nombre']}, Promedio: {estudiante['promedio']}, cantidad de calificaciones {len(estudiante['calificaciones'])}")

""" Pide indormacion al usuario para crear un estudiante y lo agrega a la lista de estudiantes """             
def ingresar_estudiante(lista_estudiantes):
    nombre = input("Ingrese el nombre del estudiante: ")
    while True: # pedimos legajo hasta que ingrese uno que o exista
        legajo = input("Ingrese el legajo del estudiante: ")
        if existe_legajo(lista_estudiantes, legajo):
            print(f"El legajo {legajo} ya está asignado a otro estudiante. Ingrese un legajo diferente.")
        else:
            break
    lista_estudiantes.append(crear_estudiante(nombre, legajo))    
    return


""" Calcula el promedio de una lista de calificaciones. Recibe como entrada un list cuyas enttrdas son float , pertenecinetes a las notas"""
def calcular_promedio(estudiante):
    if len(estudiante["calificaciones"]) == 0:
        return 0.0
    return sum(estudiante["calificaciones"]) / len(estudiante["calificaciones"])

""" permire registrar un nota a un determinado estudiante, para esto pide datos al usuario"""
def registrar_nota(lista_estudiantes):  
    print("Lista de estudiantes:")
    mostrar_estudiante(lista_estudiantes)
    
    while True:
        nro_legajo = input("Ingrese el nro de legajo a ingresar nota:")
        pos_estudiante = buscar_x_legajo(lista_estudiantes, nro_legajo)
        if pos_estudiante is not None:              
            break
        else:
            print(f"No se encontró un estudiante con el legajo {nro_legajo}. Intente nuevamente.")
        

    while True:
        nva_nota = input("Ingrese la nota obtenida, debe estar entre 0 y 10 : ")
        if(nota_valida(float(nva_nota))): # asumimos que coloca un nro; sino hay que gestonar lso errores capturando bloque try ctach
            break

    lista_estudiantes[pos_estudiante]["calificaciones"].append(float(nva_nota))
    lista_estudiantes[pos_estudiante]["promedio"] = calcular_promedio(lista_estudiantes[pos_estudiante])

           
def crear_lista_estudiante():
    return []

""" agrega un determinado estudiante a la cola de atencio, la cola mantiene solo el legajo,
acá se puedo mejorar marcando a un estudiante si ya esta en la cola para prevebir duplicados, 
ya que supuestamente solo puede estar una vez en la cola"""
def agregar_estudiante_cola(cola_espera, lista_estudiantes):
    print("Lista de estudiantes:")
    mostrar_estudiante(lista_estudiantes)
    
    while True:
        nro_legajo = input("Ingrese el nro de legajo a agregar a la cola de consultas:")
        pos_estudiante = buscar_x_legajo(lista_estudiantes, nro_legajo)
        if pos_estudiante is not None:              
            break
        else:
            print(f"No se encontró un estudiante con el legajo {nro_legajo}. Intente nuevamente.")

    estudiante = lista_estudiantes[pos_estudiante]
    enqueue(cola_espera, estudiante["legajo"])
    print(f"Estudiante {estudiante['nombre']} agregado a la cola de consultas.")


def atender_consulta(cola_espera, lista_estudiantes):
    if esta_vacia(cola_espera):
        print("No hay estudiantes en la cola de consultas.")
        return

    legajo_atender = dequeue(cola_espera)
    pos_estudiante = buscar_x_legajo(lista_estudiantes, legajo_atender)
    estudiante = lista_estudiantes[pos_estudiante]
    print(f"Atendiendo consulta del estudiante: {estudiante['nombre']} (Legajo: {estudiante['legajo']})")

""" Obtiene el mejor el promedio de una coleccion de notas"""
def mejor_promedio(lista_estudiantes):
    if len(lista_estudiantes) == 0:
        return None
    mejor_estudiante = lista_estudiantes[0]
    for estudiante in lista_estudiantes[1:]: #comparacion de hermanos
        if estudiante["promedio"] > mejor_estudiante["promedio"]:
            mejor_estudiante = estudiante
    return mejor_estudiante

""" Obtiene el peor el promedio de una coleccion de notas"""
def peor_promedio(lista_estudiantes):
    if len(lista_estudiantes) == 0:
        return None
    mejor_estudiante = lista_estudiantes[0]
    for estudiante in lista_estudiantes[1:]:  #comparacion de hermanos
        if estudiante["promedio"] < mejor_estudiante["promedio"]:
            mejor_estudiante = estudiante
    return mejor_estudiante

""" Calcula el promedio de una coleccion de notas"""
def promedio_gral(lista_notas):
    return sum(lista_notas) / len(lista_notas) if len(lista_notas) > 0 else 0.0

""" Imprime estadisticas generales de la materia; informacion de sus alumnos"""
def estadisticas(lista_estudiantes, cola_espera):
    cantidad_estudiantes = len(lista_estudiantes)
    if cantidad_estudiantes == 0:
        print("No hay estudiantes para calcular estadísticas.")
        return

    print(f"Cantidad de estudiantes: {len(lista_estudiantes)}.")
    print(f"informaiocn de los estudiantes.")
    mostrar_estudiante(lista_estudiantes)

    lista_notas_generales = []
    for i, estudiante in enumerate(lista_estudiantes):
        lista_notas_generales.extend(estudiante["calificaciones"])

    print(f"Promedio general de la materia {promedio_gral(lista_notas_generales)}")

    print(f"Mejor estudiante  {mejor_promedio(lista_estudiantes)}")
    print(f"Peor estudiante  {peor_promedio(lista_estudiantes)}")    
    print(f"Cantidad de estudiantes en cola de consultas: {tamanio(cola_espera)}")




# BLOQUE PRINCIPAL, presenta el menu y ejecuta las opciones seleccionadas por el usuario
lista_estudiantes = crear_lista_estudiante() # almacena la lista de estudiante .
cola_espera = crear_cola() #cola apara atender las consultas

while True:
    print("\n--- MENU ---")
    print("1. Agregar estudiante")
    print("2. Agregar calificación a estudiante")
    print("3. Agregar estudiante cola de consultas")
    print("4. Atender siguiente consulta")
    print("5. ver estudiantes y sus promedios")
    print("6. Ver estadisticas en general.") 
    print("7. Salir")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        ingresar_estudiante(lista_estudiantes)       
    elif opcion=="2":
        registrar_nota(lista_estudiantes)
    elif opcion == "3":
        agregar_estudiante_cola(cola_espera, lista_estudiantes)
    elif opcion == "4":
        atender_consulta(cola_espera, lista_estudiantes)
    elif opcion == "5":
        mostrar_estudiante(lista_estudiantes)
    elif opcion == "6":
        print(f"Cantidad de estudiantes: {len(lista_estudiantes)}")
        if len(lista_estudiantes) > 0:
            promedio_general = sum(estudiante["promedio"] for estudiante in lista_estudiantes) / len(lista_estudiantes)
            print(f"Promedio general de todos los estudiantes: {promedio_general}")
        else:
            print("No hay estudiantes para calcular el promedio general.")    

    elif opcion == "7":
        print("Saliendo del programa...")
        break