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

def rotacion_izquierda(x):
    y = x.derecha
    t2 = y.izquierda

    # Rotación
    y.izquierda = x
    x.derecha = t2

    # Actualización de alturas
    actualizar_altura(x)
    actualizar_altura(y)

    return y

# Árbol desbalanceado tipo RR
x = Nodo(10)
x.derecha = Nodo(20)
x.derecha.derecha = Nodo(30)

actualizar_altura(x.derecha.derecha)
actualizar_altura(x.derecha)
actualizar_altura(x)

print("Altura antes:", x.altura, "Raíz:", x.clave)

x = rotacion_izquierda(x)

print("Altura después:", x.altura, "Raíz:", x.clave)
