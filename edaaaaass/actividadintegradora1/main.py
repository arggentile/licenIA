import json

from incident_service import IncidentService
from mediciones import *
from metodos import *


def volcar_data(eventos, service_eventos):
    # procesamos los eventos para encolarlo y guardarlos en el store
    for i, elEvento in enumerate(eventos):  
        service_eventos.agregar_evento(elEvento)


def pedir_origen_destino():
    """Pide origen y destino por teclado."""
    origen = input("Origen: ").strip()
    destino = input("Destino: ").strip()
    return origen, destino
 
 
def mostrar_camino_menos_saltos(service_eventos):
    opciones_validas = ["A", "B", "C", "D", "E", "F", "G", "H"]
    while True:
        origen = input("Ingrese la estación de origen (A-E): ").upper()
        destino = input("Ingrese la estación de destino (A-E): ").upper()

        if origen in opciones_validas and destino in opciones_validas:
            print("¡Opciones válidas guardadas con éxito!")
            break  # Rompe el bucle y continúa con el programa
        else:
            print(
                "Error: El origen y el destino deben estar estrictamente entre A y E. Inténtelo de nuevo.\n"
            )

    camino = service_eventos.camino_mas_corto(origen, destino)
    if camino is None:
        print(f"No existe camino entre {origen} y {destino}.")
    else:
        print(f"Camino con menos saltos: {' -> '.join(camino)} ({len(camino) - 1} saltos)")
                 
def procesar_n_eventos(service_eventos):
    cantidad = input("¿Cuántos eventos desea procesar, se permite un maximo de 10 simultaneamente? ").strip()
    if not cantidad.isdigit() or int(cantidad) == 0:
        print("Ingrese un número entero mayor a 0.")
        return
    cantidad = int(cantidad)
    if cantidad<0 or cantidad>10: 
        print("Ingrese un número entero 0 y 10.")
        return
        
    procesados = service_eventos.procesar_eventos(cantidad)
    if not procesados:
        print("No quedan eventos por procesar.")
        return
    for evento in procesados:
        print(evento.info())
    if len(procesados) < int(cantidad):
        print(f"Solo había {len(procesados)} eventos pendientes.")


def mostrar_estadisticas_busqueda(eventos):
    """ carga el dataset de pruebas pára medicoin con 1000 entradas y llama al metodo para mostrar estaditicas de medion de tiempo"""   
    eventos  = cargar_dataset_eventos("dataset.json") # dataset inicial con 100 muestras aleatorias   
    medir_busquedas(eventos)  


def mostrar_estadisticas_ordenamiento(eventos):
    """ carga el dataset de pruebas pára medicoin con 1000 entradas y llama al metodo para mostrar estaditicas de medion de tiempo"""   
    eventos  = cargar_dataset_eventos("dataset.json") # dataset inicial con 100 muestras aleatorias
    medir_ordenamientos(eventos)       


def mostrar_arbol_avl(service_eventos):
    """ Muestra el arbol AVL por id_evento """
    service_eventos.mostrar_arbol_avl()
    
def mostrar_camino_mas_corto(service_eventos):
    """ Muestra el arbol AVL por id_evento """
    opciones_validas = ["A", "B", "C", "D", "E", "F", "G", "H"]
    while True:
        origen = input("Ingrese la estación de origen (A-H): ").upper()
        destino = input("Ingrese la estación de destino (A-H): ").upper()

        if origen in opciones_validas and destino in opciones_validas:
            print("¡Opciones válidas guardadas con éxito!")
            break  # Rompe el bucle y continúa con el programa
        else:
            print(
                "Error: El origen y el destino deben estar estrictamente entre A y E. Inténtelo de nuevo.\n"
            )

    camino = service_eventos.camino_mas_corto(origen, destino)
    if camino is None:
        print(f"No existe camino entre {origen} y {destino}.")
    else:
        print(f"Camino con menos saltos: {' -> '.join(camino)} ({len(camino) - 1} saltos)")      


def mostrar_eventos_x_rango(service_eventos):
    """ Muestra los eventos que estan en un rango de id_evento """
    
    inferior = input("Ingrese el id menor ").strip()
    superior = input("Ingrese el id mayor ").strip()
    while True:
        if not inferior.isdigit() or int(inferior) == 0:
            print("Ingrese un número entero mayor a 0.")
            inferior = input("Ingrese el id menor ").strip()
            continue
        if not superior.isdigit() or int(superior) == 0:
            print("Ingrese un número entero mayor a 0.")
            superior = input("Ingrese el id mayor ").strip()
            continue
        if int(inferior) > int(superior):
            print("El id menor no puede ser mayor que el id mayor. Intente de nuevo.")
            inferior = input("Ingrese el id menor ").strip()
            superior = input("Ingrese el id mayor ").strip()
            continue
        break
    service_eventos.mostrar_eventos_por_rango(int(inferior), int(superior))    




def main():
    eventos = cargar_dataset_eventos("dataset.json")  # dataset inicial con 100 muestras aleatorias
    service_eventos = IncidentService()
    volcar_data(eventos, service_eventos)

    #MENU
    while True:
        print("\n--- MENU ---")
        print("1. Mostrar Eventos")
        print("2. Mostrar Rutas/Indicentes")
        print("3. Mostrar Caminos menos saltos entre origen / destino")        
        print("4. Mostrar Caminos más cortos (menos indicente) entre origen / destino") #iplementar en un futuro algortimo Dkjestra
        print("5. Procesar N cantidad de eventos: mostrar su info")
        print("6. Metricas metodos de busqueda")
        print("7. Metricas metodos de ordenamiento")

        print("8. Mostrar camino mas corto entre origen y destino (Dijkstra)")

        print("10. Indice AVL por id_evento: mostrar busqueda, rango y listado completo")
        print("11. Mostrar evento AVl por rango de id_evento")
                
                        
        print("S. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            service_eventos.mostrar_info_eventos() 
        elif opcion == "2":
            service_eventos.mostrar_rutas_incidentes()
        elif opcion == "3":
            mostrar_camino_menos_saltos(service_eventos)
        elif opcion== "4":
            print("Implementar a futuro")
        elif opcion == "5":
            procesar_n_eventos(service_eventos)    
        elif opcion == "6":
            mostrar_estadisticas_busqueda(eventos)
        elif opcion == "7":
            mostrar_estadisticas_ordenamiento(eventos)
        elif opcion == "8":
            mostrar_camino_mas_corto(service_eventos)
        elif opcion == "10":
            mostrar_arbol_avl(service_eventos)
        elif opcion == "11":
            mostrar_eventos_x_rango(service_eventos)
                   
        elif opcion == "S":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida, intente de nuevo.") 
    
if __name__ == '__main__':
    try:
        main()
    except Exception as error:
        print(f"Error global no controlado: {error}")
        