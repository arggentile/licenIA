datos = [ {"id": 1, "valor": 10, "etiqueta": "bajo"}, {"id": 2, "valor": 50, "etiqueta": "medio"}, {"id": 3, "valor": 15, "etiqueta": "bajo"}, {"id": 4, "valor": 80, "etiqueta": "alto"}, {"id": 5, "valor": 55, "etiqueta": "medio"}, {"id": 6, "valor": 90, "etiqueta": "alto"} ]

def agrupar_x_categoria(diccionario):
    productos_por_categoria = {} # diccionario que mantendra para cada categoria lista de nombre d eproductios
    for producto in diccionario:        
        if producto['etiqueta'] in productos_por_categoria:
            productos_por_categoria[producto['etiqueta']].append(producto)
        else:
            productos_por_categoria[producto['etiqueta']] = [producto]
    return productos_por_categoria

def calcular_promedio(lista):
    suma = 0;
    for i in lista:
        suma = suma + i['valor']
    promedio = suma / len(lista)
    return promedio

print(f"Lista de valores origen: {datos}")
agrupados = agrupar_x_categoria(datos)   
print(f"Lista de valors agrupados: {agrupados}") 
print(f"\n") 

for clave, valor in agrupados.items():
    print(f"Para la etiqueta {clave} hay valores de: {valor} , posee una cantidad de elementos {len(valor)} su prom edio es {calcular_promedio(valor)}")  # a 1, b 2, c 3
    print(f"\n") 