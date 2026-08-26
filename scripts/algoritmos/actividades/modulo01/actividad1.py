def analizar_numeros(lista_numeros):
    promedio = None
    total_datos = len(lista_numeros)
    maximo = None
    minimo  = None
    if(total_datos>0):
        lista_set = set(lista_numeros) # asumimos que son todos numeros. no viene basura
        maximo = max(lista_set)
        minimo = min(lista_set)
        total = sum(lista_set)   
        promedio = total / total_datos
    return {
        "suma": total_datos,
        "promedio": promedio,
        "maximo": maximo,
        "minimo": minimo
    }    

listado = [15 , 2, 9 , 55, 32, 10]
ret = analizar_numeros(listado)
print(ret)