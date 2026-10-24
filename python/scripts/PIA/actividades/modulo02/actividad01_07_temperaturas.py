temperaturas = [22.5, 23.1, 22.8, 25.3, 26.7, 24.2, 23.5, 22.9, 24.1, 25.8] 

def filtrar_normales(temperaturas, rango_menor, rango_mayor):
    temp_normales = [temp for temp in temperaturas if temp >= rango_menor and temp <= rango_mayor]
    return temp_normales

def filtrar_anormales(temperaturas, rango_menor, rango_mayor):
    temp_anormales = [temp for temp in temperaturas if temp < rango_menor or temp > rango_mayor]
    return temp_anormales

def promedio_temperaturas(lista_temp):
    total = 0;
    for temperatura in lista_temp:
        total = total+ temperatura
    promedio = total / len(lista_temp)
    return      promedio

# se podria haber llamado  las funciones desde acá pero quiero independencia;
# # la funciona solo se encarga de su comedtido; armar el diccionario de datos
def armar_diccionario(temperaturas, temp_normales, temp_anormales, promdio):
    dic_temperaturas = {
        "temperaturas" : temperaturas,
        "normales" : temp_normales,
        "anormales" : temp_anormales,
        "promedio" : promdio,
    }
    return dic_temperaturas

print(f" La lista de temperaturas son : {temperaturas}")   
temp_normales = filtrar_normales(temperaturas, 23.0, 25.0)
temp_anormales = filtrar_anormales(temperaturas, 23.0, 25.0)
print(f" Las temperaturas normales  son : {temp_normales}")   
print(f" Las temperaturas anormales  son : {temp_anormales}")   
#cantidad_anormals = len(temperaturas) - len (temp_normales)
cantidad_anormales = len(temp_anormales)
promedio = promedio_temperaturas(temp_normales)

print(f" La cantidad de  temperaturas anormales  son : {cantidad_anormales}")   
print(f" El promedio de temperaturas normales  son : {promedio_temperaturas(temp_normales)}")   
print(f" {armar_diccionario(temperaturas, temp_normales, temp_anormales, promedio)}") 