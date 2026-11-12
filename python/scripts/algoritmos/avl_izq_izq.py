class Nodo:
    def __init__(self, clave):
        self.clave = clave
        self.izquierda = None
        self.derecha = None
        self.altura = 1

def altura(nodo):
    if nodo is None:
        return 0
    return nodo.altura

def actualizar_altura(nodo):
    nodo.altura = 1 + max(altura(nodo.izquierda), altura(nodo.derecha))

def rotacion_derecha(y):
    x = y.izquierda
    t2 = x.derecha

    # Rotación
    x.derecha = y
    y.izquierda = t2

    # Actualización de alturas
    actualizar_altura(y)
    actualizar_altura(x)

    return x

# Árbol desbalanceado tipo LL
y = Nodo(30)
y.izquierda = Nodo(20)
y.izquierda.izquierda = Nodo(10)

actualizar_altura(y.izquierda.izquierda)
actualizar_altura(y.izquierda)
actualizar_altura(y)

print("Altura antes:", y.altura, "Raíz:", y.clave)

y = rotacion_derecha(y)

print("Altura después:", y.altura, "Raíz:", y.clave)
