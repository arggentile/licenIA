lim_menor_insuficiente = 0
lim_mayor_insuficiente = 59
lim_menor_aprobado = 60
lim_mayor_aprobado = 69
lim_menor_notable = 70
lim_mayor_notable = 84
lim_menor_sobresaliente = 85
lim_mayor_notable = 100

nota_msj_sobre_saliente = 95
mens_felicitaciones = "Felicidades, usted ha aprobado el examen"

nota_obtenida = int(input("¿ingrese la nota obtenida: "))


if  nota_obtenida >= lim_menor_insuficiente and nota_obtenida <= lim_mayor_insuficiente:
    print("Su nota es de: ", nota_obtenida, " Nota insuficiente")
elif nota_obtenida >= lim_menor_aprobado and nota_obtenida <= lim_mayor_aprobado:
    print("Su nota es de: ", nota_obtenida, " Usted ha aprobado")           
elif nota_obtenida >= lim_menor_notable and nota_obtenida <= lim_mayor_notable:
    print("Su nota es de: ", nota_obtenida,  " Usted obtubo una nota de notable")        
elif nota_obtenida >= lim_menor_sobresaliente and nota_obtenida <= lim_mayor_notable:
    print("Su nota es de: ", nota_obtenida, " Usted obtubo una nota de sobresaliente")

if nota_obtenida >= nota_msj_sobre_saliente:
        print(mens_felicitaciones)        