import heapq

cola_prioridad = []

heapq.heappush(cola_prioridad, (15, "quince") )
heapq.heappush(cola_prioridad, (8, "ocho"))
heapq.heappush(cola_prioridad, (12, "doce"))  
heapq.heappush(cola_prioridad, (7, "siete"))  
heapq.heappush(cola_prioridad, (3, "tres"))  
heapq.heappush(cola_prioridad, (30, "treinta"))  
heapq.heappush(cola_prioridad, (2, "dos")) 

print(f"Cola de prioridad inicial: {cola_prioridad }")   

