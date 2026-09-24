class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def preorden(self, nodo, resultado):
        if nodo:
            resultado.append(nodo.valor)
            self.preorden(nodo.izq, resultado)
            self.preorden(nodo.der, resultado)

    def postorden(self, nodo, resultado):
        if nodo:
            self.postorden(nodo.izq, resultado)
            self.postorden(nodo.der, resultado)
            resultado.append(nodo.valor)

    def inorden(self, nodo, resultado):
        if nodo:
            self.inorden(nodo.izq, resultado)
            resultado.append(nodo.valor)
            self.inorden(nodo.der, resultado)
                    
if __name__ == "__main__":
    # Construcción manual del árbol
    arbol = ArbolBinario()
    arbol.raiz = Nodo(1)
    arbol.raiz.izq = Nodo(2)
    arbol.raiz.der = Nodo(3)
    arbol.raiz.izq.izq = Nodo(4)
    arbol.raiz.izq.der = Nodo(5)
    arbol.raiz.izq.der.izq = Nodo(7)
    arbol.raiz.der.der = Nodo(6)

    # Preorden: raíz - izq - der
    resultado_pre = []
    arbol.preorden(arbol.raiz, resultado_pre)
    print("Preorden: ", resultado_pre)   # [1, 2, 4, 5, 7, 3, 6]

    # Inorden: izq - raíz - der
    resultado_in = []
    arbol.inorden(arbol.raiz, resultado_in)
    print("Inorden:  ", resultado_in)    # [4, 2, 7, 5, 1, 3, 6]

    # Postorden: izq - der - raíz
    resultado_post = []
    arbol.postorden(arbol.raiz, resultado_post)
    print("Postorden:", resultado_post)  # [4, 7, 5, 2, 6, 3, 1]

    # Caso borde: árbol vacío
    arbol_vacio = ArbolBinario()
    r = []
    arbol_vacio.preorden(arbol_vacio.raiz, r)
    print("Árbol vacío:", r)  # []

    # Caso borde: un solo nodo
    arbol_uno = ArbolBinario()
    arbol_uno.raiz = Nodo(42)
    r = []
    arbol_uno.inorden(arbol_uno.raiz, r)
    print("Un nodo:   ", r)  # [42]            