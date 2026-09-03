""" Contabilizador de frcunecias de palabras"""
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
    return frecuencias

def ordenar_mayores_menor(palabras):
    lista_ordenada = []
    #lo pasamos a lista para manipula  mejor la informacion, ya que el diccionario no tiene orden
    for palabra in palabras:
        lista_ordenada.append([palabra, palabras[palabra]])

    #print(f"Lista con frecuencia en lisst: {lista_ordenada}")
    
    # Ordenamos comparando pares de elemetnos,
    # obvioamente se puede usar funciones nativas y mejores optimizadas; 
    # # pero para implejmentar lo aprendido hasta el momento
    n = len(lista_ordenada)
    for i in range(n - 1):
        #agarro el primero y lo compara que el resto, despues el segundo y asi sucesivamente, se van comparando pares de hermano
        for j in range(n - 1 - i):
            # Compra hermanos y los rotas transladando el menor hacia el fondo, 
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
