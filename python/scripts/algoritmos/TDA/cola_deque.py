from collections import deque

class Cola:
    """Cola FIFO (First In, First Out) implementada con deque."""

    def __init__(self):
        self.elementos = deque()

    def enqueue(self, item):
        """Agrega un elemento al final de la cola."""
        self.elementos.append(item)

    def dequeue(self):
        """Quita y devuelve el elemento del frente. Lanza IndexError si está vacía."""
        if self.esta_vacia():
            raise IndexError("dequeue desde una cola vacía")
        return self.elementos.popleft()

    def frente(self):
        """Devuelve el elemento del frente sin quitarlo."""
        if self.esta_vacia():
            raise IndexError("peek desde una cola vacía")
        return self.elementos[0]

    def esta_vacia(self):
        return len(self.elementos) == 0

    def tamano(self):
        return len(self.elementos)

    def __len__(self):
        return len(self.elementos)