class Cola:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def enqueue(self, elemento):
        self.items.append(elemento)

    def dequeue(self):
        if not self.esta_vacia():
            return self.items.pop(0)
        return None

    def ver_frente(self):
        if not self.esta_vacia():
            return self.items[0]
        return None

    def tamanio(self):
        return len(self.items)