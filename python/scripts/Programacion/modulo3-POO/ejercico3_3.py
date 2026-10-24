from arbolesbinarios import Nodo

OPERADORES = {'+', '-', '*', '/'}


def es_hoja(nodo):
    return nodo.izquierdo is None and nodo.derecho is None


def formatear(valor):
    # Muestra 3.0 como 3, pero deja 2.5 como 2.5
    if isinstance(valor, float) and valor.is_integer():
        return str(int(valor))
    return str(valor)


def construir_desde_postfija(expresion):
    pila = []
    for token in expresion.split():
        if token in OPERADORES:
            if len(pila) < 2:
                raise ValueError(f"Faltan operandos para '{token}'")
            der = pila.pop()   # el primero que sale es el derecho
            izq = pila.pop()
            nuevo = Nodo(token)
            nuevo.izquierdo = izq
            nuevo.derecho = der
            pila.append(nuevo)
        else:
            pila.append(Nodo(float(token)))
    if len(pila) != 1:
        raise ValueError("Expresión postfija mal formada")
    return pila.pop()


def preorden(nodo, resultado):
    if nodo:
        resultado.append(formatear(nodo.valor))
        preorden(nodo.izquierdo, resultado)
        preorden(nodo.derecho, resultado)


def postorden(nodo, resultado):
    if nodo:
        postorden(nodo.izquierdo, resultado)
        postorden(nodo.derecho, resultado)
        resultado.append(formatear(nodo.valor))


def inorden(nodo, resultado):
    if nodo:
        if not es_hoja(nodo):
            resultado.append("(")
        inorden(nodo.izquierdo, resultado)
        resultado.append(formatear(nodo.valor))
        inorden(nodo.derecho, resultado)
        if not es_hoja(nodo):
            resultado.append(")")


def evaluar(nodo):
    if es_hoja(nodo):                 # caso base
        return nodo.valor
    izq = evaluar(nodo.izquierdo)     # caso recursivo
    der = evaluar(nodo.derecho)
    if nodo.valor == '+':
        return izq + der
    if nodo.valor == '-':
        return izq - der
    if nodo.valor == '*':
        return izq * der
    if nodo.valor == '/':
        if der == 0:
            raise ZeroDivisionError("División por cero")
        return izq / der
    raise ValueError(f"Operador desconocido: {nodo.valor}")


def notacion(recorrido, arbol):
    resultado = []
    recorrido(arbol, resultado)
    return " ".join(resultado)


# (expresión postfija, resultado esperado)
PRUEBAS = [
    ("7", 7),
    ("8 2 -", 6),
    ("3 5 + 2 *", 16),
    ("3 5 2 * +", 13),
    ("10 2 8 * + 3 -", 23),
    ("20 4 / 3 2 - *", 5),
    ("2 3 + 4 1 - * 6 2 / +", 18),
]

for postfija, esperado in PRUEBAS:
    arbol = construir_desde_postfija(postfija)
    valor = evaluar(arbol)
    ok = "OK" if abs(valor - esperado) < 1e-9 else "ERROR"
    print(f"Infija:   {notacion(inorden, arbol)}")
    print(f"Prefija:  {notacion(preorden, arbol)}")
    print(f"Postfija: {notacion(postorden, arbol)}")
    print(f"Resultado: {formatear(valor)} (esperado {esperado}) -> {ok}")
    print("-" * 40)

# Caso de error: división por cero
try:
    evaluar(construir_desde_postfija("5 0 /"))
except ZeroDivisionError as e:
    print(f"5 / 0 -> {e}")