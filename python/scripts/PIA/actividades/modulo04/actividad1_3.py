"""
Ejercicio 3: Análisis de dataset de estudiantes
------------------------------------------------
Simula los datos de 60 estudiantes de una institución educativa y:
  1. Agrupa por carrera y calcula el promedio de calificaciones de cada una.
  2. Identifica la carrera con mejor rendimiento académico.
  3. Filtra a los estudiantes con promedio superior a 7 que califican para beca.
"""

import numpy as np
import pandas as pd

# ---------------------------------------------------------------------------
# 1. Generación de datos simulados
# ---------------------------------------------------------------------------
np.random.seed(42)  # Semilla para obtener siempre los mismos resultados

CANTIDAD_ESTUDIANTES = 60
ANIO_ACTUAL = 2026
PROMEDIO_MINIMO_BECA = 7.0

nombres = ["Juan", "María", "Lucas", "Sofía", "Mateo", "Valentina", "Martín",
           "Camila", "Tomás", "Lucía", "Santiago", "Martina", "Joaquín",
           "Florencia", "Nicolás", "Agustina", "Facundo", "Micaela", "Franco",
           "Julieta"]
apellidos = ["González", "Rodríguez", "Gómez", "Fernández", "López", "Díaz",
             "Martínez", "Pérez", "García", "Sánchez", "Romero", "Sosa",
             "Álvarez", "Torres", "Ruiz", "Ramírez", "Flores", "Acosta"]
carreras = ["Ingeniería en Sistemas", "Medicina", "Derecho",
            "Administración", "Psicología", "Arquitectura"]

# Año de ingreso entre 2019 y 2026
anio_ingreso = np.random.randint(2019, ANIO_ACTUAL + 1, CANTIDAD_ESTUDIANTES)
anios_cursados = ANIO_ACTUAL - anio_ingreso

# Edad coherente con el año de ingreso (ingresaron entre los 18 y 22 años)
edad = 18 + anios_cursados + np.random.randint(0, 5, CANTIDAD_ESTUDIANTES)

# Materias aprobadas: entre 3 y 8 por año cursado (mínimo 0 para ingresantes)
materias_aprobadas = np.array([
    np.random.randint(3 * a, 8 * a + 1) if a > 0 else np.random.randint(0, 4)
    for a in anios_cursados
])

# Promedio de calificaciones (escala 1-10), distribución normal acotada
promedio = np.clip(np.random.normal(6.8, 1.3, CANTIDAD_ESTUDIANTES), 1, 10).round(2)

df = pd.DataFrame({
    "nombre": [f"{np.random.choice(nombres)} {np.random.choice(apellidos)}"
               for _ in range(CANTIDAD_ESTUDIANTES)],
    "edad": edad,
    "carrera": np.random.choice(carreras, CANTIDAD_ESTUDIANTES),
    "promedio": promedio,
    "materias_aprobadas": materias_aprobadas,
    "anio_ingreso": anio_ingreso,
})

pd.set_option("display.width", 120)
pd.set_option("display.max_columns", None)

print("=" * 70)
print("DATASET DE ESTUDIANTES (primeros 10 registros)")
print("=" * 70)
print(df.head(10).to_string(index=False))
print(f"\nTotal de estudiantes: {len(df)}")

# ---------------------------------------------------------------------------
# 2. Agrupación por carrera y promedio de calificaciones
# ---------------------------------------------------------------------------
resumen_carreras = (
    df.groupby("carrera")
      .agg(cantidad_estudiantes=("nombre", "count"),
           promedio_calificaciones=("promedio", "mean"),
           promedio_materias=("materias_aprobadas", "mean"),
           mejor_promedio=("promedio", "max"))
      .round(2)
      .sort_values("promedio_calificaciones", ascending=False)
)

print("\n" + "=" * 70)
print("PROMEDIO DE CALIFICACIONES POR CARRERA")
print("=" * 70)
print(resumen_carreras.to_string())

# ---------------------------------------------------------------------------
# 3. Carrera con mejor rendimiento académico
# ---------------------------------------------------------------------------
mejor_carrera = resumen_carreras["promedio_calificaciones"].idxmax()
mejor_valor = resumen_carreras.loc[mejor_carrera, "promedio_calificaciones"]

print("\n" + "=" * 70)
print("CARRERA CON MEJOR RENDIMIENTO ACADÉMICO")
print("=" * 70)
print(f"{mejor_carrera} con un promedio general de {mejor_valor}")

# ---------------------------------------------------------------------------
# 4. Estudiantes que califican para beca (promedio > 7)
# ---------------------------------------------------------------------------
becados = (
    df[df["promedio"] > PROMEDIO_MINIMO_BECA]
      .sort_values("promedio", ascending=False)
)

print("\n" + "=" * 70)
print(f"ESTUDIANTES QUE CALIFICAN PARA BECA (promedio > {PROMEDIO_MINIMO_BECA})")
print("=" * 70)
print(becados.to_string(index=False))
print(f"\nTotal de candidatos a beca: {len(becados)} "
      f"({len(becados) / len(df):.1%} del total)")

print("\nCandidatos a beca por carrera:")
print(becados["carrera"].value_counts().to_string())