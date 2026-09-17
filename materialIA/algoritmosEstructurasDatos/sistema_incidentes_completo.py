import os
import timeit
import random
import heapq
import bisect
from collections import deque

# =====================================================================
# 🛠️ 1. DISEÑO DEL SISTEMA (POO + MODULARIDAD)
# =====================================================================

class Event:
    """
    Representa un incidente en el sistema.
    Agrupa todos los atributos requeridos por el caso de negocio.
    """
    def __init__(self, event_id: int, timestamp: float, category: str, 
                 priority: int, description: str, origin: str, destination: str):
        self.event_id = event_id
        self.timestamp = timestamp
        self.category = category
        self.priority = priority  # A menor número, mayor urgencia/prioridad
        self.description = description
        self.origin = origin
        self.destination = destination

    def __lt__(self, other):
        # Criterio para PriorityQueue: Evalúa por prioridad, luego por timestamp (FIFO si empatan)
        if self.priority == other.priority:
            return self.timestamp < other.timestamp
        return self.priority < other.priority

    def __repr__(self):
        return f"Event(ID={self.event_id}, Prio={self.priority}, Cat='{self.category}')"


class Index:
    """
    Maneja índices secundarios basados en tablas de dispersión (diccionarios).
    Permite accesos inmediatos O(1) filtrando por atributos clave.
    """
    def __init__(self):
        self._category_index = {}
        self._origin_index = {}

    def index_event(self, event: Event):
        # Indexación por Categoría
        if event.category not in self._category_index:
            self._category_index[event.category] = []
        self._category_index[event.category].append(event)
        
        # Indexación por Origen
        if event.origin not in self._origin_index:
            self._origin_index[event.origin] = []
        self._origin_index[event.origin].append(event)

    def get_by_category(self, category: str) -> list:
        return self._category_index.get(category, [])

    def get_by_origin(self, origin: str) -> list:
        return self._origin_index.get(origin, [])


class RouteNetwork:
    """
    Grafo implementado mediante una Matriz de Adyacencia para el análisis vial.
    Establece las relaciones e impactos viales causados por los incidentes.
    """
    def __init__(self, nodes: list):
        self.nodes = nodes
        self.size = len(nodes)
        self.node_to_idx = {name: i for i, name in enumerate(nodes)}
        self.matrix = [[float('inf')] * self.size for _ in range(self.size)]
        for i in range(self.size):
            self.matrix[i][i] = 0.0

    def add_route(self, u: str, v: str, distance: float):
        if u in self.node_to_idx and v in self.node_to_idx:
            idx_u = self.node_to_idx[u]
            idx_v = self.node_to_idx[v]
            self.matrix[idx_u][idx_v] = distance
            self.matrix[idx_v][idx_u] = distance  # Grafo no dirigido

    def apply_incident_penalty(self, u: str, v: str, penalty: float):
        if u in self.node_to_idx and v in self.node_to_idx:
            idx_u = self.node_to_idx[u]
            idx_v = self.node_to_idx[v]
            if self.matrix[idx_u][idx_v] != float('inf'):
                self.matrix[idx_u][idx_v] += penalty
                self.matrix[idx_v][idx_u] += penalty


class EventStore:
    """
    Almacén histórico centralizado de eventos persistidos en memoria.
    Mantiene los registros para auditoría, ordenamiento y búsquedas avanzadas.
    """
    def __init__(self):
        self.events = []

    def add_event(self, event: Event):
        self.events.append(event)

    def sort_by_id_inplace(self):
        # Usado para preparar el terreno para la búsqueda binaria eficiente
        self.events.sort(key=lambda x: x.event_id)


class Router:
    """
    Orquestador del flujo operativo inmediato de incidentes (Enrutamiento).
    Implementa las estructuras de datos lineales obligatorias (TDA).
    """
    def __init__(self):
        self.buffer = deque()            # Stack o Queue estándar (FIFO)
        self.priority_queue = []         # PriorityQueue basada en un heap binario

    def receive_incident(self, event: Event):
        """Ingreso inicial al buffer temporal O(1)"""
        self.buffer.append(event)

    def route_to_priority_heap(self):
        """Extrae del buffer y lo prioriza dinámicamente según severidad O(log N)"""
        if self.buffer:
            event = self.buffer.popleft()
            heapq.heappush(self.priority_queue, event)

    def dispatch_critical(self) -> Event:
        """Despacha el incidente más urgente del sistema O(log N)"""
        if self.priority_queue:
            return heapq.heappop(self.priority_queue)
        return None


class TextAnalyzer:
    """
    Módulo encargado del escaneo de patrones textuales dentro de las descripciones.
    """
    @staticmethod
    def contains_pattern(event: Event, pattern: str) -> bool:
        return pattern.lower() in event.description.lower()


# =====================================================================
# 🔏 DEMOSTRACIÓN COMPLEMENTARIA: CRIPTOGRAFÍA RSA BÁSICA
# =====================================================================

class RSADemo:
    """Implementación demostrativa minimalista de RSA para resguardo de datos."""
    @staticmethod
    def generate_keys():
        # Valores de ejemplo fijos y válidos para fines ilustrativos (p=61, q=53)
        n = 3233
        e = 17
        d = 2753
        return (e, n), (d, n)

    @staticmethod
    def encrypt(text: str, public_key: tuple) -> list:
        e, n = public_key
        return [pow(ord(char), e, n) for char in text]

    @staticmethod
    def decrypt(cipher_coords: list, private_key: tuple) -> str:
        d, n = private_key
        return "".join([chr(pow(char, d, n)) for char in cipher_coords])


# =====================================================================
# ⏱️ 3. BÚSQUEDA, ORDENAMIENTO Y MEDICIÓN DE RENDIMIENTO
# =====================================================================

def busqueda_secuencial(event_list, target_id):
    for ev in event_list:
        if ev.event_id == target_id:
            return ev
    return None

def busqueda_binaria(ordered_event_list, target_id):
    # Usamos bisect abstrayendo las claves ordenadas
    keys = [x.event_id for x in ordered_event_list]
    idx = bisect.bisect_left(keys, target_id)
    if idx < len(ordered_event_list) and ordered_event_list[idx].event_id == target_id:
        return ordered_event_list[idx]
    return None

def ordenamiento_burbuja(arr_copy):
    n = len(arr_copy)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr_copy[j].event_id > arr_copy[j+1].event_id:
                arr_copy[j], arr_copy[j+1] = arr_copy[j+1], arr_copy[j]
    return arr_copy

def ordenamiento_quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x.event_id < pivot.event_id]
    middle = [x for x in arr if x.event_id == pivot.event_id]
    right = [x for x in arr if x.event_id > pivot.event_id]
    return ordenamiento_quicksort(left) + middle + right


# =====================================================================
# 🚀 FUNCIÓN PRINCIPAL: LABORATORIO DE EJECUCIÓN Y PRUEBAS
# =====================================================================

if __name__ == "__main__":
    print("=" * 70)
    print("      PLATAFORMA INTEGRAL DE ANÁLISIS DE INCIDENTES Y RUTAS          ")
    print("=" * 70)
    
    # --- Configuración del Grafo viales ---
    ciudades = ["Terminal", "Centro", "Acceso_Oeste", "Puerto", "Aeropuerto"]
    red = RouteNetwork(ciudades)
    red.add_route("Terminal", "Centro", 5.0)
    red.add_route("Centro", "Acceso_Oeste", 12.0)
    red.add_route("Acceso_Oeste", "Aeropuerto", 25.0)
    red.add_route("Centro", "Puerto", 8.5)
    
    # --- Inserción y Flujo en TDA Lineales ---
    router = Router()
    store = EventStore()
    indexador = Index()
    
    # Creación de Incidentes de Prueba
    ev1 = Event(104, 1694700001, "Accidente", 2, "Choque múltiple en el Centro", "Centro", "Terminal")
    ev2 = Event(101, 1694700002, "Clima", 1, "Inundación severa en Acceso Oeste", "Acceso_Oeste", "Aeropuerto")
    ev3 = Event(109, 1694700003, "Seguridad", 3, "Objeto sospechoso en la terminal", "Terminal", "Centro")
    
    print("
[INFO] Encolando incidentes al buffer operativo (Queue: deque)...")
    router.receive_incident(ev1)
    router.receive_incident(ev2)
    router.receive_incident(router.buffer[0]) # Dummy duplicate test
    router.buffer.pop() # Limpiar duplicado dummy
    router.receive_incident(ev3)
    
    print(f"Estado del Buffer Inicial FIFO: {list(router.buffer)}")
    
    print("
[INFO] Moviendo incidentes al selector de prioridades (PriorityQueue: heapq)...")
    while router.buffer:
        router.route_to_priority_heap()
        
    print("
[INFO] Despachando incidentes bajo estricto orden de severidad:")
    while router.priority_queue:
        despachado = router.dispatch_critical()
        print(f" -> Despachando Urgente: {despachado} | Descripción: {despachado.description}")
        # Almacenar de forma histórica e indexar
        store.add_event(despachado)
        indexador.index_event(despachado)
        
    # Aplicar penalización al grafo según el incidente ocurrido en Acceso_Oeste -> Aeropuerto
    print("
[INFO] Penalizando tramo afectado en la Matriz de Adyacencia vial...")
    red.apply_incident_penalty("Acceso_Oeste", "Aeropuerto", penalty=15.5)
    
    # Mostrar fila representativa de la matriz
    idx_centro = red.node_to_idx["Centro"]
    print(f"Fila del nodo 'Centro' en la Matriz de Adyacencia: {red.matrix[idx_centro]}")
    
    # --- Demostración Encriptación RSA ---
    pub, priv = RSADemo.generate_keys()
    original_desc = "Choque"
    encriptado = RSADemo.encrypt(original_desc, pub)
    desencriptado = RSADemo.decrypt(encriptado, priv)
    print(f"
[DEMO RSA] Original: '{original_desc}' -> Encriptado: {encriptado} -> Desencriptado: '{desencriptado}'")

    # =====================================================================
    # EXPERIMENTACIÓN EMPÍRICA (TIMEIT SOBRE TAMAÑOS CRECIENTES)
    # =====================================================================
    print("
" + "=" * 70)
    print("                EXPERIMENTACIÓN Y MEDICIONES (TIMEIT)               ")
    print("=" * 70)
    
    tamanos = [100, 500, 1000]
    
    for t in tamanos:
        print(f"
>>> Evaluando estructura para N = {t} incidentes <<<")
        # Generación aleatoria controlada
        dataset_test = []
        for i in range(t):
            dataset_test.append(Event(
                event_id=random.randint(1, t * 10),
                timestamp=1694700000 + i,
                category=random.choice(["Accidente", "Clima", "Seguridad"]),
                priority=random.randint(1, 5),
                description="Alerta de transeúnte en zona de conflicto",
                origin=random.choice(ciudades),
                destination=random.choice(ciudades)
            ))
            
        # Para búsqueda binaria necesitamos copia estrictamente ordenada
        dataset_ordenado = sorted(dataset_test, key=lambda x: x.event_id)
        id_buscado = dataset_ordenado[-1].event_id  # Peor de los casos (final de la lista)
        
        # Medir Búsquedas (100 ejecuciones)
        t_sec = timeit.timeit(lambda: busqueda_secuencial(dataset_test, id_buscado), number=100)
        t_bin = timeit.timeit(lambda: busqueda_binaria(dataset_ordenado, id_buscado), number=100)
        print(f"  [BÚSQUEDA]  Secuencial: {t_sec:.6f}s | Binaria (Bisect): {t_bin:.6f}s")
        
        # Medir Ordenamiento (1 ejecución debido al costo cuadrático de burbuja)
        t_burbuja = timeit.timeit(lambda: ordenamiento_burbuja(dataset_test.copy()), number=1)
        t_quick = timeit.timeit(lambda: ordenamiento_quicksort(dataset_test.copy()), number=1)
        t_builtin = timeit.timeit(lambda: sorted(dataset_test.copy(), key=lambda x: x.event_id), number=1)
        print(f"  [ORDENAMIENTO] Burbuja O(N²): {t_burbuja:.6f}s | Quicksort O(N log N): {t_quick:.6f}s | Built-in (Timsort): {t_builtin:.6f}s")
