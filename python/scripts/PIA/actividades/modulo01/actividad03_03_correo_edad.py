def controlar_edad(edad):
    if edad < 0:
        return False
    return True    

def controlar_correeo(correo):
    deteccion_arroba = False
    deteccion_punto = False
     # lo valido asi ya que solo la idea es usar lo aprendido hasta el momento
     # Se podría haber mejorado con alguna funcion de str con split y otras funciones expresiones regulares   
    for letra in correo:
        if (letra == "@"):
            deteccion_arroba = True
        if (letra == "." and deteccion_arroba==True):
            deteccion_punto = True
                    
    return deteccion_punto

def controlar_altura(altura):
    return (altura>=0.5 and altura<=2.5)


valido = False
while valido == False:
    edad = int(input("ingrese su edad: "))
    altura = float(input("ingrese su altura la misma debe estar comprendida eentre 0.5 y 2.5: "))
    correo_electronico = input("ingrese su correo electrónico: ")
    if(controlar_edad(edad) and controlar_correeo(correo_electronico) and controlar_altura(altura)):
        print("Ingreso correctamente los tres datos")
        valido = True
    else:
        print("Datos no validos")
            