def convertir_celcius_fahrenheit(temperatura):
    return (temperatura * 9/5) + 32

def convertir_fahrenheit_celcius(temperatura):
    return (temperatura - 32) * 5/9

def convertir_celcius_kelvin(temperatura):
    return temperatura + 273.15 

def menu():
    while True:
        print("Seleccione la conversión de temperatura:")
        print("1. Celsius a Fahrenheit")
        print("2. Fahrenheit a Celsius")
        print("3. Celsius a Kelvin")
        print("4. Salir")
        opcion = input("Ingrese el número de la opción deseada: ")
        if opcion == "1":     
            temperatura = float(input("Ingrese la temperatura en Celsius: "))
            print(f"La temperatura en Fahrenheit es: {convertir_celcius_fahrenheit(temperatura)}")
        elif opcion == "2":
            temperatura = float(input("Ingrese la temperatura en Fahrenheit: "))
            print(f"La temperatura en Celsius es: {convertir_fahrenheit_celcius(temperatura)}")
        elif opcion == "3":
            temperatura = float(input("Ingrese la temperatura en Celsius: "))
            print(f"La temperatura en Kelvin es: {convertir_celcius_kelvin(temperatura)}")
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, ingrese un número válido.")
menu()