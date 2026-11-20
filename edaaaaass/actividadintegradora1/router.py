"""
Como la plataforma analiza incidentes, modelamos el peso de cada arista como la cantidad de incidentes registrados en ese tramo origen→destino. De esta manera, Dijkstra devuelve la ruta con menor acumulación de incidentes entre dos centros (ruta más segura), y Kruskal construye el árbol de expansión mínima que conecta todos los centros minimizando la exposición total a tramos conflictivos.
"""
from collections import deque
import heapq


class Vertice:
    def __init__(self, id_vertice):
        self.id_vertice = id_vertice
        self.vecinos = {}
    
    def agregar_vecino(self, vecino):
        # agregar vecino al vertice/nodeo o incrementa los incidentes entre esas rutas
        if (vecino in self.vecinos):
            self.vecinos[vecino] +=1
        else:    
            self.vecinos[vecino] = 1

    def eliminar_vecino(self, vecino):
        if vecino not in self.vecinos:
            return False
        self.vecinos[vecino] -= 1
        if self.vecinos[vecino] <= 0:
            del self.vecinos[vecino]
        return True

    def obtener_vecinos(self):
        return list(self.vecinos.keys())

    def obtener_peso(self, vecino):
        return self.vecinos.get(vecino, None)


class Router:
    def __init__(self):
        self.vertices = {}
    
    def _agregar_vertice(self, id_vertice):
        if id_vertice not in self.vertices:
            self.vertices[id_vertice] = Vertice(id_vertice)
            return True
        return False
    
   
    def agregar_incidente(self, origen, destino):
        """ Agrega un incidente entre origen y destino, y construye un grafo de rutas no dirigido  """
        self._agregar_vertice(origen)
        self._agregar_vertice(destino)
        self.vertices[origen].agregar_vecino(destino)
        self.vertices[destino].agregar_vecino(origen)

    def obtener_vecinos(self, id_vertice):
        vertice = self.vertices.get(id_vertice)
        if vertice:
            return vertice.obtener_vecinos()
        return []
    
    
    def eliminar_incidente(self, origen, destino):
        """ Se resta un incidente entre los los nodos """
        if origen not in self.vertices or destino not in self.vertices:
            return False
        
        eliminar_origen =  self.vertices[origen].eliminar_vecino(destino)
        eliminar_destino =  self.vertices[destino].eliminar_vecino(origen)                
        return eliminar_origen and eliminar_destino


    def dfs(self, inicio):
        """
        Recorrido en profundidad (iterativo) desde 'inicio'.
        Devuelve la lista de vertices visitados en el orden en que fueron descubiertos.

        Usa una PILA (LIFO) para explorar siempre el ultimo nodo descubierto.
        Equivalente a BFS pero cambiando cola por pila.

        Complejidad: O(V + E).  V = cantidad de vertices, E = cantidad de aristas.
        """
        if inicio not in self.vertices:
            return []

        visitados = set()
        pila = [inicio]       # usamos una lista como pila (append / pop al final)
        resultado = []

        while len(pila) > 0:
            vertice_actual = pila.pop()   # LIFO: saca el ultimo que entro

            # Puede que un mismo vertice se haya metido mas de una vez en la pila
            # antes de ser visitado, por eso chequeamos aca.
            if vertice_actual in visitados:
                continue

            visitados.add(vertice_actual)
            resultado.append(vertice_actual)

            # Metemos los vecinos para explorarlos despues.
            # Como es una pila, el ultimo apilado se procesa primero.
            for vecino in self.obtener_vecinos(vertice_actual):
                if vecino not in visitados:
                    pila.append(vecino)

        return resultado
    
    def bfs(self, inicio):
        """ deveulve una lista de los vertices visitados en orden de recorrido BFS desde el vertice inicio """
        if inicio not in self.vertices:
            return []

        cola = deque()
        cola.append(inicio)
        visitados = set()
        visitados.add(inicio)
        resultado = []

        while len(cola) > 0:
            vertice_actual = cola.popleft()
            resultado.append(vertice_actual)

            for vecino in self.obtener_vecinos(vertice_actual):
                if vecino not in visitados:
                    visitados.add(vecino)
                    cola.append(vecino)
        return resultado


    def dijkstra(self, origen):
        """
        Camino de MENOR COSTO (menor cantidad acumulada de incidentes) desde 'origen'
        hacia todos los demas vertices.

        Idea general (estrategia greedy):
        1. distancia[origen] = 0, el resto = infinito.
        2. Heap de pares (distancia_tentativa, vertice). Arranca con (0, origen).
        3. Se extrae el vertice con menor distancia tentativa; cuando sale del heap
            por primera vez, su distancia ya es la MINIMA definitiva (propiedad de Dijkstra).
        4. Para cada vecino, si pasar por el vertice actual mejora la distancia
            conocida al vecino, se actualiza y se inserta en el heap.

        Requiere pesos NO NEGATIVOS (la cantidad de incidentes cumple esto).

        Complejidad: O((V + E) * log V) usando heapq.

        Devuelve dos diccionarios:
        - distancias[v] : menor costo acumulado desde origen hasta v (inf si inalcanzable)
        - previos[v]    : vertice anterior a v en el camino optimo (para reconstruirlo)
        """
        if origen not in self.vertices:
            return {}, {}

        distancias = {v: float("inf") for v in self.vertices}
        previos    = {v: None          for v in self.vertices}
        distancias[origen] = 0

        # Heap de tuplas (distancia_acumulada, vertice). heapq es un min-heap.
        heap = [(0, origen)]

        while len(heap) > 0:
            dist_actual, vertice_actual = heapq.heappop(heap)

            # Si al sacarlo del heap su distancia es mayor que la que ya conocemos,
            # significa que es una entrada "vieja" que quedo en el heap: se descarta.
            if dist_actual > distancias[vertice_actual]:
                continue

            # Relajacion: para cada vecino, intentamos mejorar su distancia pasando
            # por vertice_actual.
            vertice_obj = self.vertices[vertice_actual]
            for vecino in vertice_obj.obtener_vecinos():
                peso = vertice_obj.obtener_peso(vecino)   # cantidad de incidentes en ese tramo
                nueva_distancia = dist_actual + peso

                if nueva_distancia < distancias[vecino]:
                    distancias[vecino] = nueva_distancia
                    previos[vecino] = vertice_actual
                    heapq.heappush(heap, (nueva_distancia, vecino))

        return distancias, previos


    def camino_mas_seguro(self, origen, destino):
        """
        Devuelve el camino con MENOS incidentes acumulados entre origen y destino.
        Si no hay camino, devuelve None.
        Si origen == destino, devuelve [origen] con costo 0.

        Internamente corre Dijkstra desde el origen y reconstruye el camino
        siguiendo los 'previos' hacia atras desde el destino.
        """
        if origen not in self.vertices or destino not in self.vertices:
            return None

        distancias, previos = self.dijkstra(origen)

        if distancias[destino] == float("inf"):
            return None   # inalcanzable

        # Reconstruccion del camino (del destino hacia atras usando 'previos')
        camino = []
        nodo = destino
        while nodo is not None:
            camino.append(nodo)
            nodo = previos[nodo]
        camino.reverse()

        return camino, distancias[destino]
    
    def camino_menos_saltos(self, inicio, destino):
        """ devuelve el camino con menos saltos entre incidentes (incidentes) entre el origen y el destino, si no hay camino devuelve None """
        if inicio not in self.vertices or destino not in self.vertices:
            print("No se encontro origen y/o destino")
            return None
        if inicio == destino:
            return [inicio]

        visitados = set()
        cola =deque()
        cola.append(inicio)
        visitados.add(inicio)
        padres = {inicio: None}

        while len(cola) > 0:
            vertice_actual = cola.popleft()
            if vertice_actual == destino:
                camino = []
                nodo = destino
                while nodo is not None:
                    camino.append(nodo)
                    nodo = padres[nodo]
                return camino[::-1]
            for vecino in self.obtener_vecinos(vertice_actual):
                if vecino not in visitados:
                    visitados.add(vecino)
                    padres[vecino] = vertice_actual
                    cola.append(vecino)
        return None        

    def mostrar(self):       
        if not self.vertices:
            return ""
        
        info_rutas=""
        for id_vertice in self.vertices:
            vertice = self.vertices[id_vertice]
            conexiones = [f"{v}(peso:{vertice.obtener_peso(v)})"
            for v in vertice.obtener_vecinos()]
            info_rutas += f"{id_vertice} → {';'.join(conexiones)}\n"
        return     info_rutas

if __name__ == "__main__":
    rutas = Router()
    rutas.agregar_incidente("A", "C")
    rutas.agregar_incidente("B", "C")
    rutas.agregar_incidente("C", "D")
    rutas.agregar_incidente("E", "F")
    rutas.agregar_incidente("F", "A")
    rutas.agregar_incidente("F", "A")
    rutas.agregar_incidente("A", "C")
    rutas.agregar_incidente("B", "C")
    rutas.agregar_incidente("C", "A")
    rutas.agregar_incidente("B", "C")
    rutas.agregar_incidente("B", "E")   
    rutas.agregar_incidente("E", "D")  
    
    print(f"\n Rutas: {rutas.mostrar()}")
    print(f"\n Rutas: {rutas.camino_menos_saltos('A', 'B')}")
    print(f"\n Rutas: {rutas.camino_menos_saltos('A', 'C')}")
    print(f"\n Rutas: {rutas.camino_menos_saltos('A', 'D')}")
    print(f"\n Rutas: {rutas.camino_menos_saltos('A', 'E')}")
    print(f"\n Rutas: {rutas.camino_menos_saltos('A', 'F')}")
    print(f"\n Rutas: {rutas.camino_menos_saltos('E', 'C')}")
    print(f"\n Rutas: {rutas.camino_menos_saltos('F', 'C')}")
    print(f"\n Rutas: {rutas.camino_menos_saltos('E', 'A')}")

    print(f"\n Ruta de caminos desde A: {rutas.bfs("A")}")
    print(f"\n Ruta de caminos desde D: {rutas.bfs("D")}")

    print(f"\n dijkstra: {rutas.dijkstra("A")}")