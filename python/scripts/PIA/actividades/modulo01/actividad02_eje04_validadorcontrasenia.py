password = input("¿ingrese su password: ")

if len(password) < 8:
    print("La contraseña es demasiado corta. Debe tener al menos 8 caracteres.")
elif " " in password:
    print("La contraseña no puede contener espacios en blanco.")
