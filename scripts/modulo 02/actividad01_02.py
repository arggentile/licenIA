
texto  = "inteligencia artificial machine learning deep learning artificial neural networks machine learning"

def convertir_minusculas(texto):
    return texto.lower()

def dividir_en_palabra(texto):
    return texto.split()

def contar_frecuencia_palabras(texto):
    frecuencias = {}
    for palabra in texto:
        if palabra in frecuencias:
            frecuencias[palabra] += 1
        else:
            frecuencias[palabra] = 1
            #podiamos a ver usado la funcion get con el retorno de parametrpo por defecto
            # frecuencias[palabra] = frecuencias.get(palabra, 0) + 1
    return frecuencias

def ordenar_mayores_menor(palabras):
    lista_ordenada = []
    #lo pasamos a lista para manipula r mejor la informaiocn
    for palabra in palabras:
        lista_ordenada.append([palabra, palabras[palabra]])

    # Ordenamos comparando pares de elemetnos,
    # obvioamente se puede usar funciones nativas y mejores optimizadas; 
    # # pero para implejmentar lo aprendido hasta el momento
    n = len(lista_ordenada)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            # Comparamos hermanos . Si el de la izquierda tiene menor frecuencia que el de la derecha, 
            if lista_ordenada[j][1] < lista_ordenada[j + 1][1]:
                temporal = lista_ordenada[j]
                lista_ordenada[j] = lista_ordenada[j + 1]
                lista_ordenada[j + 1] = temporal        

    return lista_ordenada    

lista_palabras = dividir_en_palabra( convertir_minusculas(texto))
print(f"Lista con palabras: {lista_palabras}")
frecuencia_palabras = contar_frecuencia_palabras(lista_palabras)
print(f"Lista con frecuencias: {frecuencia_palabras}")

lista_ordenada = ordenar_mayores_menor(frecuencia_palabras)
print(f"Cantidad de palabras en el texto: (mayor a menor): {lista_ordenada}")
