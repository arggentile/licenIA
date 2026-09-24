def calcular_promedio(lista_numeros):
    suma = 0
    for numero in lista_numeros:
        suma = suma + numero
    promedio = suma / len(lista_numeros)    
    return promedio


def encontrar_maximo(lista_numeros):
    maximo = 0
    for numero in lista_numeros:
        if numero > maximo:
            maximo = numero
    return maximo


def encontrar_minimo(lista_numeros):
    minimo = lista_numeros[0]
    for numero in lista_numeros:
        if numero < minimo:
            minimo = numero
    return minimo


def contar_pares(lista_numeros):
    cantidad = 0
    for numero in lista_numeros:
        if numero % 2 == 0:
            cantidad = cantidad + 1
    return cantidad


def contar_impares(lista_numeros):
    cantidad = 0
    for numero in lista_numeros:
        if numero % 2 != 0:
            cantidad = cantidad + 1
    return cantidad


# Programa principal
numeros = []

print("Ingrese números enteros para analizar (0 para finalizar):")

numero = int(input("Ingrese un número: "))
while numero != 0:
    numeros.append(numero)
    numero = int(input("Ingrese un número: "))

# Verificamos que se haya ingresado al menos un número
if len(numeros) == 0:
    print("No se ingresaron números para analizar.")
else:
    promedio = calcular_promedio(numeros)
    maximo = encontrar_maximo(numeros)
    minimo = encontrar_minimo(numeros)
    pares = contar_pares(numeros)
    impares = contar_impares(numeros)

    print("--- Resultados del análisis ---")
    print("Números ingresados:", numeros)
    print("Cantidad de números:", len(numeros))
    print("Promedio:", promedio)
    print("Máximo:", maximo)
    print("Mínimo:", minimo)
    print("Cantidad de pares:", pares)
    print("Cantidad de impares:", impares)