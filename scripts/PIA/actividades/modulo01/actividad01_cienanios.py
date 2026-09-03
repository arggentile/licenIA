#Escriba un programa que le pida al usuario que ingrese su nombre y su edad, y luego calcule en qué año cumplirá 100 años. El programa debe mostrar un mensaje como:
nombre = input("¿ingrese su Nombre: ")
edad = input("Ingrese su edad: ")

# se podria obtenr con alguna libreria de fecha y hora, pero para este caso lo pedimos al usuario
anio_actual = input("Ingrese el año actual: ")

anios_restante = int(anio_actual) + (100 - int(edad))
print(nombre + ", cumplirás 100 años en el año " + str(anios_restante))
