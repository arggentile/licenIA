import time


inicio = time.time()
cola = []
cola.append("1")
cola.append("2")
cola.append("3")
cola.append("4")
cola.append("6")
cola.append("2")
cola.append("33")
cola.append("d")
cola.append("1")
cola.append("2")
cola.append("3")
cola.append("4")
cola.append("6")
cola.append("2")
cola.append("33")
cola.append("d")
print(f"Elemtno eliminado {cola.pop(0)}")

fin = time.time()
print(f"Tamaño: {cola} - Tiempo:", fin - inicio)