#MEJORAR

def solicitar_entero_positivo(mensaje):   
    while True:
        numero = int(input(mensaje))
        if numero > 0:
            return numero
        print("Error: debe ser un número mayor a 0.")
       

def solicitar_calificacion(numero):
    """Solicita una calificación entre 0 y 100."""
    while True:
        nota = float(input(f"Ingrese la calificación #{numero} presione S para salir: "))
        if 0 <= nota <= 100:
            return nota
        elif nota=="S": 
            return False
        print("Error: la calificación debe estar entre 0 y 100.")
        

print("Gestion de calificaciones")

nombre = input("Ingrese el nombre del estudiante: ")
cantidad = solicitar_entero_positivo("¿Cuántas calificaciones va a ingresar? ")

calificaciones = []
salir_programa = False
for i in range(1, cantidad + 1):
    nota = solicitar_calificacion(i)
    if(nota==False):
        salir_programa = True 
        break
    calificaciones.append(nota)

if(salir_programa):
    print("Saliendo del programa...")
    exit()

promedio = sum(calificaciones) / len(calificaciones)
estado = "APROBADO" if promedio >= 60 else "REPROBADO"

# Reporte final
print("\n" + "=" * 45)
print("           REPORTE DE CALIFICACIONES")
print("=" * 45)
print(f"Estudiante:      {nombre}")
print(f"Calificaciones:  {', '.join(f'{n:.1f}' for n in calificaciones)}")
print(f"Cantidad:        {len(calificaciones)}")
print(f"Nota más alta:   {max(calificaciones):.1f}")
print(f"Nota más baja:   {min(calificaciones):.1f}")
print(f"Promedio:        {promedio:.2f}")
print(f"Estado:          {estado}")
print("=" * 45)


