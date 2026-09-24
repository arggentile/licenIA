import heapq

def dijkstra(grafo, origen):
    """
    grafo: dict donde grafo[nodo] = [(vecino, peso), ...]
    origen: nodo inicial
    Retorna: (distancias, predecesores)
    """


    # Inicialización: distancia infinita a todos, 0 al origen
    distancias = {nodo: float('inf') for nodo in grafo}
    
    distancias[origen] = 0
    print(f"Distancias iniciales: {distancias}")
    predecesores = {nodo: None for nodo in grafo}
    print(f"predecesores: {predecesores}")
    visitados = set()
    print(f"Visitados: {visitados}")

    # Cola de prioridad: (distancia_acumulada, nodo)
    cola = [(0, origen)]


    while cola:
        dist_actual, nodo_actual = heapq.heappop(cola)
        print(f"Procesando nodo: {nodo_actual}, distancia: {dist_actual}")

        # Si ya lo visitamos, saltamos (puede haber duplicados en la cola)
        if nodo_actual in visitados:
            print(f"Nodo {nodo_actual} ya visitado, saltando.")
            continue
        visitados.add(nodo_actual)
        
        # Revisar vecinos y "relajar" aristas
        for vecino, peso in grafo[nodo_actual]:
            if vecino in visitados:
                continue
            nueva_dist = dist_actual + peso
            if nueva_dist < distancias[vecino]:
                distancias[vecino] = nueva_dist
                predecesores[vecino] = nodo_actual
                heapq.heappush(cola, (nueva_dist, vecino))
        print(f"Distancias actualizadas: {distancias}")
        print(f"Predecesores actualizadas: {predecesores}")
        print(f"Nodo {nodo_actual} marcado como visitado. Visitados: {visitados}")

                
    return distancias, predecesores


def reconstruir_camino(predecesores, origen, destino):
    """Reconstruye el camino más corto desde origen hasta destino."""
    camino = []
    actual = destino
    while actual is not None:
        camino.append(actual)
        actual = predecesores[actual]
    camino.reverse()
    return camino if camino[0] == origen else []


# ---------- Ejemplo usando el mismo grafo de la visualización ----------
grafo = {
    'A': [('B', 6), ('D', 1)],
    'B': [('A', 6), ('D', 2), ('C', 5), ('E', 2)],
    'C': [('B', 5), ('E', 5)],
    'D': [('A', 1), ('B', 2), ('E', 1)],
    'E': [('B', 2), ('D', 1), ('C', 5)],
}
print(f"Grafo de ejemplo:{grafo}")

distancias, predecesores = dijkstra(grafo, 'A')


print("Distancias mínimas desde A:")
for nodo, d in sorted(distancias.items()):
    print(f"  A → {nodo}: {d}")

print("\nCamino más corto de A a C:")
print(" → ".join(reconstruir_camino(predecesores, 'A', 'C')))