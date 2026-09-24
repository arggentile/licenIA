import heapq

class ColaPrioridadTareas:
    def __init__(self):
        # Inicializa la lista que se usará como heap
        self._heap = []
        # Contador único para desempatar tareas con la misma prioridad
        self._contador = 0

    def insertar(self, tarea, prioridad):
        """Inserta una tarea con una prioridad dada."""
        # Se usa -prioridad para simular un max-heap usando el min-heap de heapq
        # La tupla es (prioridad_invertida, contador, tarea)
        elemento = (-prioridad, self._contador, tarea)
        heapq.heappush(self._heap, elemento)
        self._contador += 1
        print(f"Tarea añadida: '{tarea}' (Prioridad: {prioridad})")

    def consultar_maxima(self):
        """Consulta la tarea con mayor prioridad sin extraerla."""
        if not self._heap:
            print("La cola está vacía.")
            return None
        
        prioridad_invertida, _, tarea = self._heap[0]
        # Volvemos a invertir la prioridad para mostrar el valor original
        return tarea, -prioridad_invertida

    def extraer_maxima(self):
        """Extrae y devuelve la tarea con mayor prioridad."""
        if not self._heap:
            print("Error: No hay tareas para extraer.")
            return None
        
        prioridad_invertida, _, tarea = heapq.heappop(self._heap)
        return tarea, -prioridad_invertida


# --- Ejemplo de uso del componente ---
if __name__ == "__main__":
    cola = ColaPrioridadTareas()

    # 1. Insertar tareas (algunas con prioridad idéntica)
    cola.insertar("Escribir reporte técnico", prioridad=3)
    cola.insertar("Corregir bug crítico en producción", prioridad=10)
    cola.insertar("Responder correos rutinarios", prioridad=1)
    cola.insertar("Actualizar documentación", prioridad=3)  # Misma prioridad que el reporte

    print("-" * 40)

    # 2. Consultar la máxima prioridad actual
    proxima_tarea = cola.consultar_maxima()
    if proxima_tarea:
        print(f"Próxima tarea a realizar: '{proxima_tarea[0]}' con prioridad {proxima_tarea[1]}")

    print("-" * 40)

    # 3. Extraer las tareas en orden de prioridad
    print("Extrayendo tareas en orden de importancia:")
    while cola._heap:
        tarea, prioridad = cola.extraer_maxima()
        print(f"-> Ejecutando: '{tarea}' [Prioridad: {prioridad}]")
