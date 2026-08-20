""" Funciones de pila (LIFO) """
def crear_pila():
    return []

def esta_vacia(pila):
    return len(pila) == 0

def push(pila, elemento):
    pila.append(elemento)

def pop(pila):
    if not esta_vacia(pila):
        return pila.pop()
    return None

def ver_tope(pila):
    if not esta_vacia(pila):
        return pila[-1]
    return None

def tamanio(pila):
    return len(pila)


# invertimos una lista de elementos
def invertir_lista(lista):
    pila = crear_pila()
    
    for elemento in lista:
        push(pila, elemento)
    # sacamos los elementos de la pila y armamos una nueva lista en el orden invsero s la original 
    lista_invertida = []
    while not esta_vacia(pila):
        lista_invertida.append(pop(pila))
    
    return lista_invertida


# --- IInvierte una cadema de textpo usando funciones de pila
def invertir_cadena(texto):
    pila = crear_pila()
  
    for caracter in texto:
        push(pila, caracter)    
   
    texto_invertido = ""
    while not esta_vacia(pila):
        texto_invertido += pop(pila)
    
    return texto_invertido


lista_numeros = [1, 2, 3, 4, 5]
print(f"Lista original:   {lista_numeros}")
print(f"Lista invertida:  {invertir_lista(lista_numeros)}")

cadena_original = "Inteligencia Artificial"
print(f"Cadena original:  {cadena_original}")
print(f"Cadena invertida: {invertir_cadena(cadena_original)}")