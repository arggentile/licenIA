estudiantes = [
{ 
  "nombre": "Armando", 
  "edad": 36, 
  "carrera": "ingenieria en Sistemas",
  "promedio": 8.5
},
{ 
  "nombre": "lucrecia", 
  "edad": 23, 
  "carrera": "Abogacia",
  "promedio": 9.25
},
{ 
  "nombre": "Ruiz", 
  "edad": 30, 
  "carrera": "Ingenieria en Sistemas",
  "promedio": 7.5
},
{ 
  "nombre": "Sebastian", 
  "edad": 22, 
  "carrera": "lic. en IA",
  "promedio": 8.0
}
]

def mayores_al_promedio(estudiantes, promedio):
    sobresalientes = [est for est in estudiantes if est["promedio"] >= promedio]
    return sobresalientes

def promedio_gral(estudiantes):
    total_notas = 0   
    for elemento in estudiantes:
        total_notas = total_notas + elemento["promedio"]
    promedio_total = total_notas / len(estudiantes)     
    return     promedio_total
                
   
def mejor_promedio(estudiantes):
    mejor_notas = 0
    mejor_estudiante = {}   
    for elemento in estudiantes:
        if(mejor_notas < elemento["promedio"]):
            mejor_notas = elemento["promedio"]
            mejor_estudiante = elemento

    return mejor_estudiante 

print(f"Los estudiantes son : {estudiantes}")
promedio = 8.5
print(f"Los estudiantes destacados con prmedio mayor a {promedio} son : {mayores_al_promedio(estudiantes, promedio)}")
print(f"El promedio general es : {promedio_gral(estudiantes)}")
print(f"Emejor estudiante es:  : {mejor_promedio(estudiantes)}")
