# cuenta la cantidad de vocales en una frase
def tabla_multiplicar(base, limite=10):
    for i in range(1, limite + 1):
        print(f"{base} x {i} = {base * i}")
                
def maquina():
    while True:
        base = int(input("Ingrese un número para ver su tabla de multiplicar (0 para salir): "))
        if(base == 0):    
            break
        limite = int(input("Ingrese el limite hasta multiplicar: "))
        if(limite > 0) and (base > 0):
            tabla_multiplicar(base, limite)
        else:    
            print("ingrese numeros positivos")
maquina()
