# cuenta la cantidad de vocales en una frase
def contar_vocales(frase):
    cantidad = 0
    lista_vocales = ["a", "e", "i", "o", "u"] # se puede mejorar usando funciones nativas, se usa de esta manera por que es lo que se vio hasta el momento
    for letra in frase:
        for una_vocal in lista_vocales:
            if una_vocal == letra:
                cantidad = cantidad + 1
    return cantidad


# cuenta la cantidad de palabras en una frase
def contar_palabras(frase):
    cantidad = 0
    for letra in frase:
        if letra == " ": #se cuenta asi, ya que no se usa funciones nativas; nadie garantiza que despues de un blanco haya una letra validad que comience una palabrfa
            cantidad = cantidad + 11
    return cantidad



def convertir_fahrenheit_celcius(temperatura):
    return (temperatura - 32) * 5/9

def convertir_celcius_kelvin(temperatura):
    return temperatura + 273.15 

frae = input("Ingrese una frase: ")