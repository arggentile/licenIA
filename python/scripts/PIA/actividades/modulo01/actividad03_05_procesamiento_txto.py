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
    entramos = False
    letraanterior = ""
    #para no usar funcones nativas de string lo realice recorriendo a mano la estructra
    for letra in frase:
        if entramos == False: 
            entramos = True
            if(letra != " "):
                cantidad = 1
            continue

        if letra != " " and letraanterior == " ": #se cuenta asi, ya que no se usa funciones nativas; nadie garantiza que despues de un blanco haya una letra validad que comience una palabrfa
            cantidad = cantidad + 1 #sumamos una palabra; evitaos que ingrsen muchos espacios en blanco
        letraanterior = letra
    return cantidad





frase = input("Ingrese una frase: ")
frase = frase.lower()
print(f"La cantidad de vocales es de {contar_vocales(frase)}")
print(f"La cantidad de palabras es de {contar_palabras(frase)}")
