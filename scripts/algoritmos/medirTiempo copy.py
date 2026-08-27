from collections import deque
import time

inicio = time.time()
colas = deque()
colas.append("1")
colas.append("2")
colas.append("3")
colas.append("4")
colas.append("6")
colas.append("2")
colas.append("33")
colas.append("d")
colas.append("1")
colas.append("2")
colas.append("3")
colas.append("4")
colas.append("6")
colas.append("2")
colas.append("33")
colas.append("d")

print(f"Elemtno eliminado {cola.popleft()}")
fin = time.time()
print(f"Tamaño: {cola} - Tiempo:", fin - inicio)

"""

def suma_for(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

def suma_formula(n):
    return n * (n + 1) // 2

n = 1000000

inicio = time.time()
suma_for(n)
fin = time.time()
print("Tiempo suma con for:", fin - inicio)

inicio1 = time.time()
suma_formula(n)
fin1 = time.time()
print("Tiempo suma con fórmula:", fin1 - inicio1)
"""


""" a--- """

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