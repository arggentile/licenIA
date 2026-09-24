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

def es_numero(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
    
# se define de forma sencilla una calculadora para realizar operaciones
def calculadora(numero1, numero2, operador):
    match operador:
        case '+':
            return numero1 + numero2
        case '-':
            return numero1 - numero2
        case '/':
            return numero1 / numero2
        case '*':
            return numero1 * numero2
            
# recibe una lista en notacion pstfijas para operarla y retornan un valor
def evaluar_espresion_postfijas(lista_operar):    
    operandos = crear_pila()  
    operadores = ("+","-","*","/") # asi agregamos la cantidad de operador que deseamos

    for valor in lista_operar:
        #verificamos si es digito o un operador valido
        if(valor not in operadores and (not es_numero(valor) ) ):
            print(f"operacion no valida, operadores no validos")
            return 
        if(es_numero(valor)):
            push(operandos, float(valor))
        elif(valor in operadores):
            if(tamanio(operandos)<2): # se puede mejorar        
                print("Error: faltan parametros numericos para realizar la operación")
                return
            numero1 =  pop(operandos)
            numero2 =  pop(operandos)
            operacion = calculadora(numero2, numero1, valor)
            push(operandos, operacion)

    return operandos

expresion1 =  ["5", "3", "+", "2", "*"]
print(f"La expresion {expresion1} su resultado es:  {evaluar_espresion_postfijas(expresion1)}")
expresion2 =   ["15", "7", "+", "3", "/"]
print(f"La expresion {expresion2} su resultado es:  {evaluar_espresion_postfijas(expresion2)}")