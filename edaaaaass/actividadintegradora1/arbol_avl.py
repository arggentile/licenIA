class Nodo:
    """ Nodo de un arbol AVL. Guarda clave, valor, hijos y altura del subarbol. """
    def __init__(self, clave, valor=None):
        self.clave = clave
        self.valor = valor          
        self.izquierda = None
        self.derecha = None
        self.altura = 1             


class ArbolAvl:
    """
    Arbol binario de busqueda AUTO-BALANCEADO (AVL).

    En todo nodo, la diferencia de alturas entre el subarbol
    izquierdo y el derecho no puede superar a 1 (factor de balance en {-1, 0, 1}).

    Si tras una insercion o una eliminacion el factor de balance de un nodo se vuelve 2 o -2,
    se aplica una rotacion para restaurar el balance:

      - Desbalance izquierda-izquierda (LL)  -> rotacion simple a derecha
      - Desbalance derecha-derecha  (RR)     -> rotacion simple a izquierda
      - Desbalance izquierda-derecha (LR)    -> rotacion doble: izq del hijo, der del padre
      - Desbalance derecha-izquierda (RL)    -> rotacion doble: der del hijo, izq del padre

    Complejidad:
      - Insercion: O(log n)
      - Busqueda:  O(log n)
      - Recorrido in-orden: O(n) y devuelve las claves en orden ascendente.
    """

    def __init__(self):
        self.raiz = None
        self._cantidad = 0

    # -------------------- utilitarios --------------------
    def _altura(self, nodo):
        """ Altura segura: 0 si el nodo es None. """
        if nodo is None:
            return 0
        return nodo.altura

    def _balance(self, nodo):
        """ Factor de balance = altura(izq) - altura(der). """
        if nodo is None:
            return 0
        return self._altura(nodo.izquierda) - self._altura(nodo.derecha)

    def _actualizar_altura(self, nodo):
        """ Recalcula la altura del nodo a partir de sus hijos. """
        nodo.altura = 1 + max(self._altura(nodo.izquierda), self._altura(nodo.derecha))

    # -------------------- rotaciones --------------------
    def _rotar_derecha(self, y):
        """
        Rotacion simple a la derecha. Usada cuando el subarbol izquierdo esta
        mas alto y el desbalance viene del hijo izquierdo-izquierdo (LL).        
        """
        x = y.izquierda
        derecha_a_rotar = x.derecha

        x.derecha = y
        y.izquierda = derecha_a_rotar

        self._actualizar_altura(y)
        self._actualizar_altura(x)
        return x  # nueva raiz del subarbol

    def _rotar_izquierda(self, x):
        """
        Rotacion simple a la izquierda. Usada cuando el subarbol derecho esta
        mas alto y el desbalance viene del hijo derecho-derecho (RR).
        """
        y = x.derecha
        izquierda_a_rotar = y.izquierda

        y.izquierda = x
        x.derecha = izquierda_a_rotar

        self._actualizar_altura(x)
        self._actualizar_altura(y)
        return y  # nueva raiz del subarbol

    # -------------------- insercion --------------------
    def insertar(self, clave, valor=None):
        """ Inserta clave/valor manteniendo la propiedad AVL. O(log n). """
        self.raiz = self._insertar_recursivo(self.raiz, clave, valor)

    def _insertar_recursivo(self, nodo, clave, valor):
        # 1. Insercion estandar de BST
        if nodo is None:
            self._cantidad += 1
            return Nodo(clave, valor)

        if clave < nodo.clave:
            nodo.izquierda = self._insertar_recursivo(nodo.izquierda, clave, valor)
        elif clave > nodo.clave:
            nodo.derecha = self._insertar_recursivo(nodo.derecha, clave, valor)
        else:
            # clave ya existente: actualizamos el valor y no incrementamos cantidad
            nodo.valor = valor
            return nodo

        # 2. Actualizamos altura
        self._actualizar_altura(nodo)

        # 3. Verificamos balance y aplicamos rotaciones si corresponde
        balance = self._balance(nodo)

        # Caso LL: el desbalance viene de la izquierda del hijo izquierdo
        if balance > 1 and clave < nodo.izquierda.clave:
            return self._rotar_derecha(nodo)

        # Caso RR: el desbalance viene de la derecha del hijo derecho
        if balance < -1 and clave > nodo.derecha.clave:
            return self._rotar_izquierda(nodo)

        # Caso LR: el desbalance viene de la derecha del hijo izquierdo
        if balance > 1 and clave > nodo.izquierda.clave:
            nodo.izquierda = self._rotar_izquierda(nodo.izquierda)
            return self._rotar_derecha(nodo)

        # Caso RL: el desbalance viene de la izquierda del hijo derecho
        if balance < -1 and clave < nodo.derecha.clave:
            nodo.derecha = self._rotar_derecha(nodo.derecha)
            return self._rotar_izquierda(nodo)

        return nodo

    # -------------------- busqueda --------------------
    def buscar(self, clave):
        """ Devuelve el valor asociado a la clave, o None si no existe. O(log n). """
        nodo = self._buscar_recursivo(self.raiz, clave)
        return nodo.valor if nodo is not None else None

    def _buscar_recursivo(self, nodo, clave):
        if nodo is None or nodo.clave == clave:
            return nodo
        if clave < nodo.clave:
            return self._buscar_recursivo(nodo.izquierda, clave)
        return self._buscar_recursivo(nodo.derecha, clave)

    def contiene(self, clave):
        return self._buscar_recursivo(self.raiz, clave) is not None

    # -------------------- recorridos --------------------
    def inorden(self):
        """ Recorrido in-orden: devuelve [(clave, valor), ...] en orden ascendente. """
        resultado = []
        self._inorden_recursivo(self.raiz, resultado)
        return resultado

    def _inorden_recursivo(self, nodo, acumulador):
        if nodo is None:
            return
        self._inorden_recursivo(nodo.izquierda, acumulador)
        acumulador.append((nodo.clave, nodo.valor))
        self._inorden_recursivo(nodo.derecha, acumulador)

    def rango(self, clave_min, clave_max):
        """
        Devuelve todos los (clave, valor) cuya clave esta en [clave_min, clave_max].
        Aprovecha el orden del AVL para no recorrer todo el arbol.
        O(log n + k) donde k es la cantidad de elementos en el rango.
        """
        resultado = []
        self._rango_recursivo(self.raiz, clave_min, clave_max, resultado)
        return resultado

    def _rango_recursivo(self, nodo, lo, hi, acumulador):
        if nodo is None:
            return
        if lo < nodo.clave:
            self._rango_recursivo(nodo.izquierda, lo, hi, acumulador)
        if lo <= nodo.clave <= hi:
            acumulador.append((nodo.clave, nodo.valor))
        if nodo.clave < hi:
            self._rango_recursivo(nodo.derecha, lo, hi, acumulador)

    def cantidad(self):
        return self._cantidad

    def altura_arbol(self):
        return self._altura(self.raiz)


if __name__ == "__main__":
    arbol = ArbolAvl()

    ids = [614827, 738201, 205544, 391877, 582039, 946715,
           417206, 853990, 672188, 239074, 508623, 760451]

    for id_ev in ids:
        arbol.insertar(id_ev, f"Evento#{id_ev}")

    print(f"Cantidad insertada: {arbol.cantidad()}")
    print(f"Altura del arbol  : {arbol.altura_arbol()}  (si no fuera AVL podria llegar a {len(ids)})")

    print("\nRecorrido in-orden (ordenado por id):")
    for clave, valor in arbol.inorden():
        print(f"  {clave} -> {valor}")

    print("\nBusquedas:")
    print(f"  buscar(508623) = {arbol.buscar(508623)}")
    print(f"  buscar(99999)  = {arbol.buscar(99999)}")

    print("\nRango de ids entre 400000 y 700000:")
    for clave, valor in arbol.rango(400000, 700000):
        print(f"  {clave} -> {valor}")