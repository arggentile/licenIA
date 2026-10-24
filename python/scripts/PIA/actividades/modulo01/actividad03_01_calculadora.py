def suma(num1, num2):
    return num1 + num2

def resta(num1, num2):
    return num1 - num2

def multiplicacion(num1, num2):
    return num1 * num2

def potencia(base, exponente):
    return base ** exponente

def division(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return None

def calculadora():
    while True:
        numero1 = float(input("Ingrese el primer número: "))
        numero2 = float(input("Ingrese el segundo número: "))
        print("Seleccione la operación:")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Potencia")
        print("6. Salir")

        opcion = int(input("Ingrese el número de la operación deseada: "))
        print("Opcion elegida es " ,opcion)

        if opcion == 1:
            resultado = suma(numero1, numero2)
            print(f"El resultado de la suma es: {resultado}")
        elif opcion == 2:
            resultado = resta(numero1, numero2)
            print(f"El resultado de la resta es: {resultado}")
        elif opcion == 3:
            resultado = multiplicacion(numero1, numero2)
            print(f"El resultado de la multiplicación es: {resultado}")
        elif opcion == 4:
            resultado = division(numero1, numero2)
            if resultado is not None:
                print(f"El resultado de la división es: {resultado}")
            else:
                print("Error: División por cero no permitida.")
        elif opcion == 5:
            resultado = potencia(numero1, numero2)
            print(f"El resultado de la potencia es: {resultado}")
        elif opcion == 6:
            print("Saliendo de la calculadora.")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")      

calculadora()