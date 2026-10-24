limite_peso_bajo = 18.5
limite_peso_normal = 24.9   
limite_peso_sobrepeso = 29.9
limite_peso_obesidad = 30     

altura = input("¿ingrese su altura: ")
peso = input("¿ingrese su peso: ")
peso = float(peso)
altura_al_cuadrado = float(altura) ** 2 # float(altura) * float(altura)
imc_paciente = peso / altura_al_cuadrado

if  imc_paciente < limite_peso_bajo:
    print("Su imc es: ", imc_paciente, " el limite del IMC es: ", limite_peso_bajo, " El paciente tiene bajo peso")
elif imc_paciente >= limite_peso_bajo and imc_paciente <= limite_peso_normal:
    print("Su imc es: ", imc_paciente, " el limite del IMC es: ", limite_peso_normal, "El paciente tiene peso normal")
elif imc_paciente > limite_peso_normal and imc_paciente <= limite_peso_sobrepeso:
    print("Su imc es: ", imc_paciente, " el limite del IMC es: ", limite_peso_sobrepeso, "El paciente tiene sobrepeso")        
elif imc_paciente > limite_peso_obesidad:
    print("Su imc es: ", imc_paciente, " el limite del IMC es: ", limite_peso_obesidad, "El paciente tiene obesidad")    
