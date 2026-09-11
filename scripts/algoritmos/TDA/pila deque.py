from collections import deque
class Pila:
    """Pila LIFO (Last In, First Out) implementada con deque."""

    def __init__(self):
        self.elementos = deque()

    def push(self, item):
        """Apila un elemento en el tope."""
        self.elementos.append(item)

    def pop(self):
        """Desapila y devuelve el elemento del tope. Lanza IndexError si está vacía."""
        if self.esta_vacia():
            raise IndexError("pop desde una pila vacía")
        return self.elementos.pop()

    def tope(self):
        """Devuelve el tope sin desapilarlo."""
        if self.esta_vacia():
            raise IndexError("peek desde una pila vacía")
        return self.elementos[-1]

    def esta_vacia(self):
        return len(self.elementos) == 0

    def tamano(self):
        return len(self.elementos)

    def __len__(self):
        return len(self.elementos)