from grafos import Grafo

class RedSocial:
    def __init__(self):
        self.grafo = Grafo(dirigido=False)
        self.usuarios = {}

    def agregar_usuario(self, id, nombre):
        self.grafo.agregar_vertice(id)
        self.usuarios[id] = nombre

    def agregar_amistad(self, usuario1, usuario2):
        self.grafo.agregar_arista(usuario1, usuario2)

    def obtener_amigos(self, usuario):
        return self.grafo.obtener_vecinos(usuario)

    def sugerir_amigos(self, usuario):
        amigos = set(self.obtener_amigos(usuario))
        sugerencias = {}
        for amigo in amigos:
            amigos_del_amigo = self.obtener_amigos(amigo)
        for candidato in amigos_del_amigo:
            if candidato != usuario and candidato not in amigos:
                if candidato not in sugerencias:
                    sugerencias[candidato] = 0
                sugerencias[candidato] += 1    

        sugerencias_ordenadas = sorted(sugerencias.items(), key=lambda x: x[1], reverse=True)
        return [(self.usuarios[id], count) for id, count in sugerencias_ordenadas]

    def grado_separacion(self, usuario1, usuario2):
        camino = self.grafo.camino_mas_corto(usuario1, usuario2)
        if camino:
            return len(camino) - 1
        return None
    
if __name__ == "__main__":
    print("=== Probando Red Social ===\n")
    red = RedSocial()
    red.agregar_usuario("u1", "Ana")
    red.agregar_usuario("u2", "Carlos")
    red.agregar_usuario("u3", "Beatriz")
    red.agregar_usuario("u4", "Diego")
    red.agregar_usuario("u5", "Elena")
    red.agregar_usuario("u6", "Franco")
    red.agregar_amistad("u1", "u2")
    red.agregar_amistad("u1", "u3")
    red.agregar_amistad("u2", "u4")
    red.agregar_amistad("u3", "u4")
    red.agregar_amistad("u3", "u5")
    red.agregar_amistad("u4", "u6")
    print(f"Amigos de Ana: {[red.usuarios[id] for id in red.obtener_amigos('u1')]}")
    print("\nSugerencias de amistad para Ana:")
    sugerencias = red.sugerir_amigos("u1")
    for nombre, conexiones_comunes in sugerencias:
        print(f" {nombre} ({conexiones_comunes} amigos en común)")
    print(f"\nGrados de separación entre Ana y Franco: {red.grado_separacion('u1', 'u6')}")
    print("\n¡Pruebas completadas!")