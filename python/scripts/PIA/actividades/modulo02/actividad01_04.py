muestra_a = {"edad", "altura", "peso", "presion"}
muestra_b = {"edad", "peso", "temperatura", "frecuencia_cardiaca"}
muestra_c = {"altura", "peso", "edad", "glucosa"}

interseccion = muestra_a & muestra_b & muestra_c
print(f"Características comunes a todas las muestras (intersección de los tres). {interseccion}")

distitnivo_de_a = muestra_a - muestra_b - muestra_c
print(f"Características únicas de muestra_a (que no están en b ni en c).. {distitnivo_de_a}")

union = muestra_a | muestra_b | muestra_c
print(f"Todas las características diferentes observadas (unión de todas). {union}")


simetria = muestra_a | muestra_b | muestra_c
print(f"Cantidad total de características únicas. {simetria}")


