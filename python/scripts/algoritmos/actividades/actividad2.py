# Este programa calcula estadísticas de temperaturas 
import statistics 
# Función para convertir Celsius a Fahrenheit 
def celsius_a_fahrenheit(celsius): 
    """Convierte temperatura de Celsius a Fahrenheit""" 
    return (celsius * 9/5) + 32 

def calcular_estadisticas(lista_temperaturas):
    promedio = sum(lista_temperaturas) / len(lista_temperaturas)
    desviacion = statistics.stdev(datos_celsius) 
    return promedio, desviacion

# Código principal 
datos_celsius = [20, 22, 18, 25, 19] 
print("Temperaturas en Celsius:", datos_celsius)

promedio, desviacion = calcular_estadisticas(datos_celsius)

print(f"Promedio: {promedio:.2f}°C")

print(f"Desv. Estándar: {desviacion:.2f}")

datos_fahrenheit = [celsius_a_fahrenheit(t) for t in datos_celsius] 
print("Temperaturas en Fahrenheit:", datos_fahrenheit) 
