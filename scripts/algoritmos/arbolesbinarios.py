class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    # 1. INSERTAR
    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._insertar_recursivo(self.raiz, valor)

    def _insertar_recursivo(self, nodo_actual, valor):
        if valor < nodo_actual.valor:
            if nodo_actual.izquierdo is None:
                nodo_actual.izquierdo = Nodo(valor)
            else:
                self._insertar_recursivo(nodo_actual.izquierdo, valor)
        else:
            if nodo_actual.derecho is None:
                nodo_actual.derecho = Nodo(valor)
            else:
                self._insertar_recursivo(nodo_actual.derecho, valor)

    # 2. ELIMINAR
    def eliminar(self, valor):
        self.raiz = self._eliminar_recursivo(self.raiz, valor)

    def _eliminar_recursivo(self, nodo_actual, valor):
        if nodo_actual is None:
            return nodo_actual

        # Buscar el nodo
        if valor < nodo_actual.valor:
            nodo_actual.izquierdo = self._eliminar_recursivo(nodo_actual.izquierdo, valor)
        elif valor > nodo_actual.valor:
            nodo_actual.derecho = self._eliminar_recursivo(nodo_actual.derecho, valor)
        else:
            # Nodo encontrado: Caso 1 (Sin hijos) o Caso 2 (Un hijo)
            if nodo_actual.izquierdo is None:
                return nodo_actual.derecho
            elif nodo_actual.derecho is None:
                return nodo_actual.izquierdo

            # Caso 3: Dos hijos (Buscar el menor del subárbol derecho)
            nodo_actual.valor = self._minimo_valor(nodo_actual.derecho)
            # Eliminar el sucesor
            nodo_actual.derecho = self._eliminar_recursivo(nodo_actual.derecho, nodo_actual.valor)

        return nodo_actual

    def _minimo_valor(self, nodo):
        actual = nodo
        while actual.izquierdo is Node is not None:
            actual = actual.izquierdo
        return actual.valor

    # 3. MOSTRAR (En orden para ver la lógica)
    def en_orden(self):
        elementos = []
        self._en_orden_recursivo(self.raiz, elementos)
        return elementos

    def _en_orden_recursivo(self, nodo, elementos):
        if nodo:
            self._en_orden_recursivo(nodo.izquierdo, elementos)
            elementos.append(nodo.valor)
            self._en_orden_recursivo(nodo.derecho, elementos)

# --- PRUEBA DEL SCRIPT ---
arbol = ArbolBinario()
valores = [50, 30, 70, 20, 40, 60, 80]

for v in valores:
    arbol.insertar(v)

print("Árbol inicial:", arbol.en_orden()) 
# Resultado: [20, 30, 40, 50, 60, 70, 80]


arbol.eliminar(20) # Eliminar hoja
arbol.eliminar(30) # Eliminar nodo con un hijo
arbol.eliminar(50) # Eliminar la raíz (dos hijos)

print("Árbol final:", arbol.en_orden())
# Resultado ordenado sin esos números