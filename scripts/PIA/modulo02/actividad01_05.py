valores = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

#es obvia la funcion pero se descompone asi por si el dia de mañana se ambia la estrutura de datos se toca la funcion
def calcular_maximo(lista):
    return max(lista)

def calcular_minimo(lista):
    return min(lista)

def normalizar(lista, minimo,maximo):
    return [(nro - minimo) / (maximo - minimo) for nro in lista]

print(f"Lista original es: {valores}")
el_maximo  = calcular_maximo(valores)
el_minimo  = calcular_minimo(valores)

print(f"EL maximo es: {el_maximo}  el minimo es: {el_minimo}")
print(f"la lista normalizada es: {normalizar(valores, el_minimo, el_maximo)}")

