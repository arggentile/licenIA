""" Se definen como diferentes funcoinaes ya que despues se puede implementar median te POO"""
def crear_pila():
    return []

def esta_vacia(pila):
    return len(pila) == 0

def push(pila, elemento):
    pila.append(elemento)

def pop(pila):
    if not esta_vacia(pila):
        return pila.pop()
    return None

def ver_tope(pila):
    if not esta_vacia(pila):
        return pila[-1]
    return None

def tamanio(pila):
    return len(pila)

def validador_expresion_balanceada(expresion):
    expresion_valida = True
    balanceador = crear_pila() # almacenada 
    delimitadores_apertura = ("(","[","{")
    delimitadores_cierre = (")","]","}")
    for caracter in expresion:
        if caracter in delimitadores_apertura:
            push(balanceador, caracter)
            continue
        if caracter in delimitadores_cierre:
            anterior = ver_tope(balanceador)
            if (( anterior == '(' and caracter != ')') or (anterior=='[' and caracter != ']') or (anterior=='{' and caracter != '}')):
                expresion_valida = False
                break
            else:
                pop(balanceador)
    return expresion_valida

expresion1 = "{[()]}"
expresion2 = "{[(])}" 
expresion3 = "[[()]]" 
expresion4 = "((a + b) * (c - d))"

print(f"La expresion {expresion1} es {validador_expresion_balanceada(expresion1)}")
print(f"La expresion {expresion2} es  {validador_expresion_balanceada(expresion2)}")
print(f"La expresion {expresion3} es {validador_expresion_balanceada(expresion3)}")
print(f"La expresion {expresion4} es {validador_expresion_balanceada(expresion4)}")
