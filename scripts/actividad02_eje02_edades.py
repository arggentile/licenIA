edad = input("¿ingrese su edad: ")
edad = int(edad)

if edad < 0:    
    print("La edad ingresada no es válida")
elif edad >= 0 and edad <= 12:
    print("Usted es un niño")
elif edad >= 13 and edad <= 17:
    print("Usted es un adolescente")
elif edad >= 18 and edad <= 29:     
    print("Usted es un adulto joven")
elif edad >= 30 and edad <= 59:
    print("Usted es un adulto")
elif edad >= 60:
    print("Usted es un adulto mayor")    