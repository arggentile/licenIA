class Persona:
    def __init__(self, nombre, anio_nacimiento):
        self.nombre = nombre
        self.anio_nacimiento = anio_nacimiento
        self.padre = None
        self.madre = None
        self.hijos = []

    def obtener_padres(self):
        padres = []
        if self.padre is not None:
            padres.append(self.padre)
        if self.madre is not None:
            padres.append(self.madre)
        return padres

    def obtener_abuelos(self):
        abuelos = []
        for progenitor in self.obtener_padres():
            for abuelo in progenitor.obtener_padres():
                abuelos.append(abuelo)
        return abuelos

    def obtener_hermanos(self):
        hermanos = []
        for progenitor in self.obtener_padres():
            for hijo in progenitor.hijos:
                if hijo is not self and hijo not in hermanos:
                    hermanos.append(hijo)
        return hermanos

    def es_medio_hermano(self, otra):
        # Son medio hermanos si comparten solo uno de los dos padres
        mismo_padre = self.padre is not None and self.padre is otra.padre
        misma_madre = self.madre is not None and self.madre is otra.madre
        return mismo_padre != misma_madre

    def obtener_ancestros(self, max_niveles, nivel_actual=1):
        """Devuelve una lista de tuplas (persona, nivel). Nivel 1 = padres, 2 = abuelos..."""
        ancestros = []
        if nivel_actual > max_niveles:
            return ancestros
        for progenitor in self.obtener_padres():
            ancestros.append((progenitor, nivel_actual))
            ancestros.extend(progenitor.obtener_ancestros(max_niveles, nivel_actual + 1))
        return ancestros

    def todos_los_ancestros(self):
        """Todos los ancestros sin límite de niveles, sin repetir."""
        resultado = []
        for progenitor in self.obtener_padres():
            if progenitor not in resultado:
                resultado.append(progenitor)
            for ancestro in progenitor.todos_los_ancestros():
                if ancestro not in resultado:
                    resultado.append(ancestro)
        return resultado

    def __str__(self):
        return f"{self.nombre} ({self.anio_nacimiento})"


class ArbolGenealogico:
    NOMBRES_NIVEL = {1: "Padre/Madre", 2: "Abuelo/a", 3: "Bisabuelo/a", 4: "Tatarabuelo/a"}

    def __init__(self, apellido):
        self.apellido = apellido
        self.personas = {}

    def agregar_persona(self, nombre, anio_nacimiento):
        if nombre in self.personas:
            print(f"Aviso: {nombre} ya está registrado.")
            return self.personas[nombre]
        persona = Persona(nombre, anio_nacimiento)
        self.personas[nombre] = persona
        return persona

    def buscar(self, nombre):
        return self.personas.get(nombre)

    def establecer_padres(self, nombre_hijo, nombre_padre=None, nombre_madre=None):
        hijo = self.buscar(nombre_hijo)
        if hijo is None:
            print(f"Error: {nombre_hijo} no existe en el árbol.")
            return False

        if nombre_padre is not None:
            padre = self.buscar(nombre_padre)
            if padre is None:
                print(f"Error: {nombre_padre} no existe en el árbol.")
                return False
            hijo.padre = padre
            padre.hijos.append(hijo)

        if nombre_madre is not None:
            madre = self.buscar(nombre_madre)
            if madre is None:
                print(f"Error: {nombre_madre} no existe en el árbol.")
                return False
            hijo.madre = madre
            madre.hijos.append(hijo)

        return True

    # ------------------------- Consultas -------------------------

    def abuelos_de(self, nombre):
        persona = self.buscar(nombre)
        print(f"\nAbuelos de {persona}:")
        abuelos = persona.obtener_abuelos()
        if len(abuelos) == 0:
            print("  (no hay abuelos registrados)")
        for abuelo in abuelos:
            print(f"  - {abuelo}")

    def hermanos_de(self, nombre):
        persona = self.buscar(nombre)
        print(f"\nHermanos de {persona}:")
        hermanos = persona.obtener_hermanos()
        if len(hermanos) == 0:
            print("  (no tiene hermanos registrados)")
        for hermano in hermanos:
            tipo = "medio hermano/a" if persona.es_medio_hermano(hermano) else "hermano/a"
            print(f"  - {hermano} [{tipo}]")

    def ancestros_de(self, nombre, niveles):
        persona = self.buscar(nombre)
        print(f"\nAncestros de {persona} hasta {niveles} generaciones:")
        ancestros = persona.obtener_ancestros(niveles)
        if len(ancestros) == 0:
            print("  (no hay ancestros registrados)")
        for ancestro, nivel in ancestros:
            nombre_nivel = self.NOMBRES_NIVEL.get(nivel, f"Ancestro nivel {nivel}")
            print(f"  - Nivel {nivel} ({nombre_nivel}): {ancestro}")

    def son_familiares(self, nombre1, nombre2):
        p1 = self.buscar(nombre1)
        p2 = self.buscar(nombre2)

        # Se incluye a cada persona en su propia lista para detectar
        # el caso en que una es ancestro directo de la otra
        linaje1 = [p1] + p1.todos_los_ancestros()
        linaje2 = [p2] + p2.todos_los_ancestros()

        comunes = []
        for persona in linaje1:
            if persona in linaje2:
                comunes.append(persona)

        print(f"\n¿{p1.nombre} y {p2.nombre} son familiares?", end=" ")
        if len(comunes) > 0:
            nombres = ", ".join(p.nombre for p in comunes)
            print(f"SÍ. Ancestros en común: {nombres}")
            return True
        print("NO. No comparten ancestros.")
        return False

    def mostrar_descendientes(self, nombre):
        persona = self.buscar(nombre)
        print(f"\nÁrbol de descendientes de {persona.nombre}:")
        self._imprimir_descendientes(persona, 0)

    def _imprimir_descendientes(self, persona, nivel):
        if nivel == 0:
            print(persona)
        else:
            print("    " * nivel + "└─ " + str(persona))
        for hijo in persona.hijos:
            self._imprimir_descendientes(hijo, nivel + 1)

    def mostrar_ancestros(self, nombre):
        persona = self.buscar(nombre)
        print(f"\nÁrbol de ancestros de {persona.nombre}:")
        self._imprimir_ancestros(persona, 0, "")

    def _imprimir_ancestros(self, persona, nivel, etiqueta):
        print("    " * nivel + etiqueta + str(persona))
        if persona.padre is not None:
            self._imprimir_ancestros(persona.padre, nivel + 1, "Padre: ")
        if persona.madre is not None:
            self._imprimir_ancestros(persona.madre, nivel + 1, "Madre: ")


# ============================ Programa principal ============================

arbol = ArbolGenealogico("Familia González")

# Generación 1: abuelos (bisabuelos de los más chicos)
arbol.agregar_persona("José", 1930)
arbol.agregar_persona("María", 1933)
arbol.agregar_persona("Pedro", 1928)
arbol.agregar_persona("Rosa", 1932)

# Generación 2: padres
arbol.agregar_persona("Carlos", 1955)
arbol.agregar_persona("Ana", 1960)
arbol.agregar_persona("Laura", 1958)
arbol.agregar_persona("Miguel", 1957)   # esposo de Ana, sin padres registrados
arbol.agregar_persona("Elena", 1962)    # segunda pareja de Carlos

# Generación 3: hijos
arbol.agregar_persona("Juan", 1980)
arbol.agregar_persona("Sofía", 1983)
arbol.agregar_persona("Diego", 1987)    # medio hermano de Juan y Sofía
arbol.agregar_persona("Lucía", 1986)    # prima de Juan
arbol.agregar_persona("Valeria", 1982)  # esposa de Juan, no es familiar de sangre

# Generación 4: nietos
arbol.agregar_persona("Mateo", 2010)
arbol.agregar_persona("Emma", 2013)

# Persona sin relación con la familia
arbol.agregar_persona("Roberto", 1990)

# Relaciones
arbol.establecer_padres("Carlos", "José", "María")
arbol.establecer_padres("Ana", "José", "María")
arbol.establecer_padres("Laura", "Pedro", "Rosa")
arbol.establecer_padres("Juan", "Carlos", "Laura")
arbol.establecer_padres("Sofía", "Carlos", "Laura")
arbol.establecer_padres("Diego", "Carlos", "Elena")
arbol.establecer_padres("Lucía", "Miguel", "Ana")
arbol.establecer_padres("Mateo", "Juan", "Valeria")
arbol.establecer_padres("Emma", "Juan", "Valeria")

print("=" * 60)
print(f"  ÁRBOL GENEALÓGICO - {arbol.apellido.upper()}")
print(f"  Personas registradas: {len(arbol.personas)}")
print("=" * 60)

# 1. Abuelos
arbol.abuelos_de("Juan")
arbol.abuelos_de("Mateo")
arbol.abuelos_de("Carlos")

# 2. Hermanos (completos y medios hermanos)
arbol.hermanos_de("Juan")
arbol.hermanos_de("Diego")
arbol.hermanos_de("Lucía")

# 3. Ancestros por niveles
arbol.ancestros_de("Mateo", 2)
arbol.ancestros_de("Mateo", 3)

# 4. Parentesco por ancestros comunes
arbol.son_familiares("Mateo", "Lucía")    # primos segundos: comparten a José y María
arbol.son_familiares("Juan", "Diego")     # medio hermanos: comparten a Carlos
arbol.son_familiares("Emma", "Pedro")     # Pedro es bisabuelo de Emma
arbol.son_familiares("Juan", "Valeria")   # pareja, pero no familiares de sangre
arbol.son_familiares("Sofía", "Roberto")  # sin relación

# 5. Visualización del árbol
arbol.mostrar_descendientes("José")
arbol.mostrar_ancestros("Mateo")