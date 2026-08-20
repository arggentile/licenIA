lista_numeros  = [23, 45, 12, 23, 56, 89, 12, 45, 67, 23, 89, 34] 

def quitar_duplicados(lista):
    return set(lista)

def transformar_conjunto_lista(conjunto):
    return [elemento for elemento in conjunto]

# se dfine en funciones ya que si me cambian el tipo de datos el maximo debe calcularse de otra forma
def get_minimo(lista_numeros):
    return min(lista_numeros)

def get_maximo(lista_numeros):
    return max(lista_numeros)

def get_promedio(lista_numeros):
    return max(lista_numeros)

def get_obtener_promedio(lista_numeros):
    return sum(lista_numeros) / len(lista_numeros)


print(f"Lista original : {lista_numeros}")
sin_repetidos_set  = quitar_duplicados(lista_numeros)
print(f"Lista original sin repeditdos : {sin_repetidos_set}")

sin_repetidos =transformar_conjunto_lista(quitar_duplicados(lista_numeros))
sin_repetidos.sort()
#ordenamos, podiamos a ver qcreado una funcion
print(f"Ordenados : {sin_repetidos}" )

print(f"La cantidad de valores unicos: {len(sin_repetidos)}")
print(f"El maximo es  {get_maximo(sin_repetidos)}")
print(f"El minimo es  {get_minimo(sin_repetidos)}")
promedio = get_obtener_promedio(sin_repetidos)
print(f"El promedio es  {promedio}")
lista_may_promedio = [n for n in sin_repetidos if n > promedio]
print(f"puntajes mayores al promedio  son  {lista_may_promedio}")
