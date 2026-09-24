""" Se definen como diferentes funciones para pasarlo despues a POO"""
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

def crear_navegador():
    return {
        "anteriores": crear_pila(),
        "siguientes": crear_pila(),
        "pagina_actual": None
    }


def visitar(navegador, url):
    #esto es debatible, se podría hacer ignorado el if != None ya que cuando estras al navegador
    #algnos navegadores cuando visitas por primera vez y voles atras te deja en la pagina blanco
    if( navegador['pagina_actual']!= None):
        push(navegador['anteriores'], navegador['pagina_actual']) #almacenamos la pagina actual por si volvemos atras
    navegador['pagina_actual'] =  url #actualizamos la pagia actual
    #esto lo podemos obviar pero muhcos navegadores al visitar una pagina nueva ponen en vacio la pila de adelante
    navegador['siguientes'] = crear_pila()
    
def volverAtras(navegador):
    urlAnterior = pop(navegador['anteriores'])
    push(navegador['siguientes'], navegador['pagina_actual'])
    navegador['pagina_actual'] =   urlAnterior
   


def avanzar(navegador):
    #push(navegador['anteriores'], navegador['pagina_actual'])
    urlSiguiente = pop(navegador['siguientes'])
    if(urlSiguiente == None):
        print(f"No se puede avanzar, no hay más paginas")
        return
    push(navegador['anteriores'],navegador['pagina_actual'])
    navegador['pagina_actual'] =   urlSiguiente    
    #pop(navegador['siguientes'])

navegador = crear_navegador()
visitar(navegador, "google.com")
visitar(navegador, "wikipedia.org")
visitar(navegador, "github.com")
print(f"los datos del navegador son: {navegador}")
volverAtras(navegador)
volverAtras(navegador)
print(f"los datos del navegador son: {navegador}")
avanzar(navegador)
print(f"los datos del navegador son: {navegador}")
"""visitar(navegador, "stackoverflow.com")
print(f"los datos del navegador son: {navegador}")
avanzar(navegador)
"""