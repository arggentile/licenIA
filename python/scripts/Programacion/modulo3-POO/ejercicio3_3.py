from abc import ABC, abstractmethod
import operator


# ----------------------------------------------------------------------
# Condición de un nodo interno
# ----------------------------------------------------------------------
class Condicion:
    OPERADORES = {
        "==": operator.eq,
        "!=": operator.ne,
        ">": operator.gt,
        ">=": operator.ge,
        "<": operator.lt,
        "<=": operator.le,
    }

    def __init__(self, atributo, op, valor):
        if op not in self.OPERADORES:
            raise ValueError(f"Operador no soportado: {op}")
        self.atributo = atributo
        self.op = op
        self.valor = valor

    def evaluar(self, ejemplo):
        if self.atributo not in ejemplo:
            raise KeyError(f"Falta el atributo '{self.atributo}' en los datos")
        return self.OPERADORES[self.op](ejemplo[self.atributo], self.valor)

    def negada(self):
        """Texto de la condición contraria (para las reglas)."""
        contrario = {"==": "!=", "!=": "==", ">": "<=", ">=": "<", "<": ">=", "<=": ">"}
        return f"{self.atributo} {contrario[self.op]} {self.valor}"

    def __str__(self):
        return f"{self.atributo} {self.op} {self.valor}"


# ----------------------------------------------------------------------
# Nodos
# ----------------------------------------------------------------------
class Nodo(ABC):
    @abstractmethod
    def predecir(self, ejemplo, camino=None):
        """Devuelve la clase y (opcionalmente) acumula el camino recorrido."""

    @abstractmethod
    def es_hoja(self):
        pass


class NodoHoja(Nodo):
    def __init__(self, clase):
        self.clase = clase

    def predecir(self, ejemplo, camino=None):
        if camino is not None:
            camino.append(f"=> {self.clase}")
        return self.clase

    def es_hoja(self):
        return True

    def __repr__(self):
        return f"NodoHoja({self.clase!r})"


class NodoDecision(Nodo):
    def __init__(self, condicion, si, no):
        self.condicion = condicion
        self.si = si    # hijo cuando la condición es verdadera
        self.no = no    # hijo cuando la condición es falsa

    def predecir(self, ejemplo, camino=None):
        resultado = self.condicion.evaluar(ejemplo)
        if camino is not None:
            camino.append(f"¿{self.condicion}? {'Sí' if resultado else 'No'}")
        siguiente = self.si if resultado else self.no
        return siguiente.predecir(ejemplo, camino)

    def es_hoja(self):
        return False

    def __repr__(self):
        return f"NodoDecision({self.condicion})"


# ----------------------------------------------------------------------
# Árbol
# ----------------------------------------------------------------------
class ArbolDecision:
    def __init__(self, raiz=None, nombre="Árbol de decisión"):
        self.raiz = raiz
        self.nombre = nombre

    # --- construcción -------------------------------------------------
    @staticmethod
    def decision(atributo, op, valor, si, no):
        """Atajo para crear un nodo interno."""
        return NodoDecision(Condicion(atributo, op, valor), si, no)

    @staticmethod
    def hoja(clase):
        """Atajo para crear una hoja."""
        return NodoHoja(clase)

    def establecer_raiz(self, nodo):
        self.raiz = nodo
        return self

    # --- predicción ---------------------------------------------------
    def predecir(self, ejemplo):
        self._verificar()
        return self.raiz.predecir(ejemplo)

    def explicar(self, ejemplo):
        """Devuelve la predicción y el camino seguido por el árbol."""
        self._verificar()
        camino = []
        clase = self.raiz.predecir(ejemplo, camino)
        return clase, camino

    # --- evaluación ---------------------------------------------------
    def evaluar(self, datos, etiquetas):
        """Compara predicciones con resultados esperados.
        Devuelve un dict con precisión, aciertos, matriz de confusión y errores."""
        if len(datos) != len(etiquetas):
            raise ValueError("datos y etiquetas deben tener la misma longitud")
        if not datos:
            raise ValueError("No hay datos para evaluar")

        clases = sorted(set(etiquetas) | set(self.clases()), key=str)
        matriz = {real: {pred: 0 for pred in clases} for real in clases}
        aciertos, errores = 0, []

        for i, (ejemplo, esperado) in enumerate(zip(datos, etiquetas)):
            predicho = self.predecir(ejemplo)
            matriz[esperado][predicho] += 1
            if predicho == esperado:
                aciertos += 1
            else:
                errores.append((i, ejemplo, esperado, predicho))

        return {
            "precision": aciertos / len(datos),
            "aciertos": aciertos,
            "total": len(datos),
            "matriz_confusion": matriz,
            "errores": errores,
        }

    # --- exportación --------------------------------------------------
    def exportar_reglas(self):
        """Reglas SI ... ENTONCES ..., una por cada hoja."""
        self._verificar()
        reglas = []

        def recorrer(nodo, condiciones):
            if nodo.es_hoja():
                antecedente = " Y ".join(condiciones) if condiciones else "SIEMPRE"
                reglas.append(f"SI {antecedente} ENTONCES {nodo.clase}")
                return
            recorrer(nodo.si, condiciones + [str(nodo.condicion)])
            recorrer(nodo.no, condiciones + [nodo.condicion.negada()])

        recorrer(self.raiz, [])
        return reglas

    def exportar_texto(self):
        """Representación indentada del árbol."""
        self._verificar()
        lineas = [self.nombre]

        def recorrer(nodo, prefijo, etiqueta):
            if nodo.es_hoja():
                lineas.append(f"{prefijo}{etiqueta}-> [{nodo.clase}]")
                return
            lineas.append(f"{prefijo}{etiqueta}¿{nodo.condicion}?")
            nuevo = prefijo + "    "
            recorrer(nodo.si, nuevo, "Sí ")
            recorrer(nodo.no, nuevo, "No ")

        recorrer(self.raiz, "", "")
        return "\n".join(lineas)

    def guardar_reglas(self, ruta):
        with open(ruta, "w", encoding="utf-8") as f:
            f.write(self.exportar_texto() + "\n\nReglas:\n")
            for i, r in enumerate(self.exportar_reglas(), 1):
                f.write(f"R{i}: {r}\n")

    # --- utilidades ---------------------------------------------------
    def clases(self):
        resultado = set()

        def recorrer(nodo):
            if nodo.es_hoja():
                resultado.add(nodo.clase)
            else:
                recorrer(nodo.si)
                recorrer(nodo.no)

        if self.raiz:
            recorrer(self.raiz)
        return resultado

    def profundidad(self, nodo=None):
        nodo = nodo or self.raiz
        if nodo.es_hoja():
            return 0
        return 1 + max(self.profundidad(nodo.si), self.profundidad(nodo.no))

    def _verificar(self):
        if self.raiz is None:
            raise RuntimeError("El árbol no tiene raíz: constrúyalo primero")


# ----------------------------------------------------------------------
# Ejemplo: ¿llevar paraguas?
# ----------------------------------------------------------------------
def construir_arbol_paraguas():
    A = ArbolDecision
    raiz = A.decision(
        "lloviendo", "==", True,
        si=A.hoja("Llevar paraguas"),
        no=A.decision(
            "prob_lluvia", ">=", 60,
            si=A.hoja("Llevar paraguas"),
            no=A.decision(
                "prob_lluvia", ">=", 30,
                si=A.decision(
                    "temperatura", "<", 15,
                    si=A.hoja("Llevar paraguas"),     # frío + riesgo moderado
                    no=A.hoja("No llevar paraguas"),
                ),
                no=A.hoja("No llevar paraguas"),
            ),
        ),
    )
    return ArbolDecision(raiz, "Árbol: ¿Llevar paraguas?")


def imprimir_matriz(matriz):
    clases = list(matriz)
    ancho = max(len(str(c)) for c in clases) + 2
    print(" " * ancho + "Predicho →")
    print("Real ↓".ljust(ancho) + "".join(str(c).ljust(ancho) for c in clases))
    for real in clases:
        print(str(real).ljust(ancho) + "".join(str(matriz[real][p]).ljust(ancho) for p in clases))


def main():
    arbol = construir_arbol_paraguas()

    print("=" * 60)
    print(arbol.exportar_texto())
    print(f"\nProfundidad: {arbol.profundidad()}  |  Clases: {sorted(arbol.clases())}")

    print("\n" + "=" * 60)
    print("REGLAS DE DECISIÓN")
    for i, r in enumerate(arbol.exportar_reglas(), 1):
        print(f"R{i}: {r}")

    # Datos de prueba (atributos + resultado esperado)
    casos = [
        ({"lloviendo": True,  "prob_lluvia": 90, "temperatura": 12}, "Llevar paraguas"),
        ({"lloviendo": True,  "prob_lluvia": 40, "temperatura": 25}, "Llevar paraguas"),
        ({"lloviendo": False, "prob_lluvia": 80, "temperatura": 20}, "Llevar paraguas"),
        ({"lloviendo": False, "prob_lluvia": 65, "temperatura": 28}, "Llevar paraguas"),
        ({"lloviendo": False, "prob_lluvia": 45, "temperatura": 10}, "Llevar paraguas"),
        ({"lloviendo": False, "prob_lluvia": 45, "temperatura": 22}, "No llevar paraguas"),
        ({"lloviendo": False, "prob_lluvia": 10, "temperatura": 30}, "No llevar paraguas"),
        ({"lloviendo": False, "prob_lluvia": 20, "temperatura": 5},  "No llevar paraguas"),
        ({"lloviendo": False, "prob_lluvia": 55, "temperatura": 18}, "Llevar paraguas"),     # el árbol falla
        ({"lloviendo": False, "prob_lluvia": 35, "temperatura": 14}, "No llevar paraguas"),  # el árbol falla
    ]
    datos = [c[0] for c in casos]
    etiquetas = [c[1] for c in casos]

    print("\n" + "=" * 60)
    print("PREDICCIONES (con el camino recorrido)")
    for ejemplo, esperado in casos:
        pred, camino = arbol.explicar(ejemplo)
        marca = "✓" if pred == esperado else "✗"
        print(f"\n{marca} {ejemplo}")
        print("   " + "  →  ".join(camino))
        if pred != esperado:
            print(f"   (esperado: {esperado})")

    print("\n" + "=" * 60)
    print("EVALUACIÓN")
    res = arbol.evaluar(datos, etiquetas)
    print(f"Precisión: {res['precision']:.1%} ({res['aciertos']}/{res['total']})\n")
    imprimir_matriz(res["matriz_confusion"])
    if res["errores"]:
        print("\nErrores:")
        for i, ej, esp, pred in res["errores"]:
            print(f"  caso {i}: esperado '{esp}', predicho '{pred}'")

    arbol.guardar_reglas("reglas_paraguas.txt")
    print("\nReglas exportadas a reglas_paraguas.txt")


if __name__ == "__main__":
    main()