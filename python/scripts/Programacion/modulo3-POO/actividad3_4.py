class Persona:
    def __init__(self, id, nombre, edad, intereses):
        self.id = id
        self.nombre = nombre
        self.edad = edad
        self.intereses = intereses

    def __str__(self):
        return f"{self.nombre}, {self.edad} años, intereses: {', '.join(self.intereses)}"
    
class Vertice:
    def __init__(self, id):
        self.id = id
        self.vecinos = {}

    def agregar_vecino(self, vecino, peso=1):
        self.vecinos[vecino] = peso

    def obtener_vecinos(self):
        return list(self.vecinos.keys())

    def obtener_peso(self, vecino):
        return self.vecinos.get(vecino, None)

class Grafo:
    def __init__(self, dirigido=False):
        self.vertices = {}
        self.dirigido = dirigido

    def agregar_vertice(self, id):
        if id not in self.vertices:
            self.vertices[id] = Vertice(id)
            return True
        return False

    def agregar_arista(self, origen, destino, peso=1):
        if origen not in self.vertices:
            self.agregar_vertice(origen)
        if destino not in self.vertices:
            self.agregar_vertice(destino)
        self.vertices[origen].agregar_vecino(destino, peso)
        if not self.dirigido:
            self.vertices[destino].agregar_vecino(origen, peso)

    def obtener_vecinos(self, id):
        vertice = self.vertices.get(id)
        if vertice:
            return vertice.obtener_vecinos()
        return []

    def bfs(self, inicio):
        if inicio not in self.vertices:
            return []
        visitados = set()
        cola = [inicio]
        visitados.add(inicio)
        resultado = []

        while len(cola) > 0:
            vertice_actual = cola.pop(0)
            resultado.append(vertice_actual)

            for vecino in self.obtener_vecinos(vertice_actual):
                if vecino not in visitados:
                    visitados.add(vecino)
                    cola.append(vecino)
        return resultado

    def camino_mas_corto(self, inicio, destino):
        if inicio not in self.vertices or destino not in self.vertices:
            return None
        if inicio == destino:
            return [inicio]

        visitados = set()
        cola = [inicio]
        visitados.add(inicio)
        padres = {inicio: None}

        while len(cola) > 0:
            vertice_actual = cola.pop(0)

            if vertice_actual == destino:
                camino = []
                nodo = destino
                while nodo is not None:
                    camino.append(nodo)
                    nodo = padres[nodo]
                return camino[::-1]

            for vecino in self.obtener_vecinos(vertice_actual):
                if vecino not in visitados:
                    visitados.add(vecino)
                    padres[vecino] = vertice_actual
                    cola.append(vecino)

        return None     

    def mostrar(self):
        for id_vertice in self.vertices:
            vertice = self.vertices[id_vertice]
            conexiones = [f"{v}(peso:{vertice.obtener_peso(v)})"
            for v in vertice.obtener_vecinos()]
            print(f"{id_vertice} → {'', ''.join(conexiones)}")


class RedSocial:
    def __init__(self):
        self.grafo = Grafo(dirigido=False)
        self.usuarios = {}

    def agregar_usuario(self, persona):
        self.grafo.agregar_vertice(persona.id)
        self.usuarios[persona.id] = persona

    def agregar_amistad(self, idPersona1, idPersona2):
        self.grafo.agregar_arista(idPersona1, idPersona2)
    
    def obtener_amigos(self, idPersona):
        return self.grafo.obtener_vecinos(idPersona)
    
    def sugerir_amigos(self, idPersona):       
        amigos = set(self.obtener_amigos(idPersona))
        sugerencias = {}
        for amigo in amigos:
            amigos_del_amigo = self.obtener_amigos(amigo)
            for candidato in amigos_del_amigo:        
                if candidato != idPersona and candidato not in amigos:
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
    redSocial = RedSocial()

    # Crear personas
    ana   = Persona(1, "Ana", 25, ["música", "cine"])
    bruno = Persona(2, "Bruno", 30, ["fútbol", "videojuegos"])
    carla = Persona(3, "Carla", 22, ["lectura", "música"])
    diego = Persona(4, "Diego", 28, ["cine", "fotografía"])
    elena = Persona(5, "Elena", 35, ["viajes", "cocina"])
    fede  = Persona(6, "Fede", 27, ["programación", "videojuegos"])

    # Agregarlas a la red
    for p in [ana, bruno, carla, diego, elena, fede]:
        redSocial.agregar_usuario(p)

    # Crear amistades
    redSocial.agregar_amistad(1, 2)
    redSocial.agregar_amistad(1, 3)
    redSocial.agregar_amistad(2, 5)
    redSocial.agregar_amistad(3, 4)
    redSocial.agregar_amistad(4, 5)
    redSocial.agregar_amistad(5, 6)

    print("=== Grafo ===")
    redSocial.grafo.mostrar()

    print("\n=== Usuarios ===")
    for persona in redSocial.usuarios.values():
        print(persona)

    print("\n=== Amigos de Ana ===")
    for id_amigo in redSocial.obtener_amigos(1):
        print("-", redSocial.usuarios[id_amigo].nombre)

    print("\n=== Sugerencias para Ana ===")
    for persona, comunes in redSocial.sugerir_amigos(1):
        print(f"- {persona.nombre} ({comunes} amigos en común)")

    print("\nGrado de separación Ana → Fede:", redSocial.grado_separacion(ana, fede))
