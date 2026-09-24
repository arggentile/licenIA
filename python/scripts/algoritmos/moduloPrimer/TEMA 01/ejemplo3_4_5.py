for i in range(5):
    print("Iteración:", i)

def suma_naturales(n):
    suma = 0
    for i in range(1, n + 1):
        suma += i
    return suma

resultado = suma_naturales(10)
print("Resultado:", resultado)

print("")
print("")

def es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

print(es_par(8))
print(es_par(7))