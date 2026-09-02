import time


def sumar_n_cantidad_elementos(n_cantidad):
    inicio = time.time()
    total_acumulado = 0
    for i in range(n_cantidad):
        total_acumulado += i

    fin = time.time()
    tiempoejecucion = fin  - inicio
    return total_acumulado, tiempoejecucion

    

total_diez_elementos, tiempo_diez_elementos = sumar_n_cantidad_elementos(10)
total_mil_elementos, tiempo_mil_elementos = sumar_n_cantidad_elementos(1000)
print(f"La suma de 10 elem,entos es de {total_diez_elementos} tiempo {tiempo_diez_elementos}")
print(f"La suma de 1000 elem,entos es de {total_mil_elementos} tiempo {tiempo_mil_elementos}")