# 1) IMPORTACIÓN DE MÓDULOS (en este ejemplo no es estrictamente necesario,
# pero se incluye para mostrar la estructura)
import time

# 2) DEFINICIÓN DE FUNCIONES
def suma_lista(numeros):
    """Devuelve la suma de todos los elementos de una lista."""
    total = 0
    for n in numeros:
        total += n
    return total

def maximo_lista(numeros):
    """Devuelve el valor máximo de una lista."""
    maximo = numeros[0]
    for n in numeros:
        if n > maximo:
            maximo = n
    return maximo

# 3) CÓDIGO PRINCIPAL
if __name__ == "__main__":
    datos = [3, 7, 2, 9, 4]

    inicio = time.time()

    suma = suma_lista(datos)
    maximo = maximo_lista(datos)

    fin = time.time()

    print("Datos:", datos)
    print("Suma:", suma)
    print("Máximo:", maximo)
    print("Tiempo de ejecución (segundos):", fin - inicio)
