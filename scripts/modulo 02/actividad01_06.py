valores =  [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

def minimo(listas):
    return min(listas)

def maximo(listas):
    return max(listas)

def normalizar(lista, minimo, maximo):
    return [(numero - minimo) / (maximo - minimo) for numero in lista ]

lista_normalizada = normalizar(valores, minimo(valores), maximo(valores))

print(f"La lista original es: {valores}")
print(f"Minimo es: {minimo(valores)}")
print(f"Maximo es: {maximo(valores)}")

print(f"La lista normalizada  es: {lista_normalizada}")
