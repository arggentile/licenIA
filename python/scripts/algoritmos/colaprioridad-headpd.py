import heapq

cola_prioridsad = []
print(f"{cola_prioridsad}")
heapq.heappush(cola_prioridsad, 5 )
heapq.heappush(cola_prioridsad, 2 )
heapq.heappush(cola_prioridsad, 8 )
heapq.heappush(cola_prioridsad, 1 )
print(f"{cola_prioridsad}")
print(f"Elemento con mayor prioridad: {heapq.heappop(cola_prioridsad)}")
print(f"{cola_prioridsad}")
print(f"Elemento con mayor prioridad: {heapq.heappop(cola_prioridsad)}")
print(f"{cola_prioridsad}")
