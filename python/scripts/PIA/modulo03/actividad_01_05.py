class Materia:
    def __init__(self, codigo, nombre, nota_aprobacion, nota_minima, nota_maxima):
        self.nombre = nombre
        self.codigo = codigo
        self.nota_aprobacion = nota_aprobacion
        self.nota_minima = nota_minima
        self.nota_maxima = nota_maxima
     # podemosimplementar metodos y más definiciones
    def getCodigo(self):
        return self.codigo
    
class MateriaNota:
    def __init__(self, materia, nota):
        self.materia = materia
        self.nota = nota

    def getMateria(self):
        return self.materia
    
    def getNota(self):
        return self.nota

    def registrarNota(self, nota):
        self.nota = nota
    
class Estudiante:
    def __init__(self, nombre, apellido, dni, carrera, nota_aprobacion, nota_minima, nota_maxima):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.carrera = carrera
        self.materias = []  # del tipo MateriaNota

    #define si esta inscripto un aluimno o no
    def estoy_inscripto_materia(self, nuevaMateria):
        for pos, mater in  enumerate(self.materias):
            matNota = mater.getMateria()
            if(nuevaMateria.getCodigo() == matNota.getCodigo()):
                return True
        return False        

    def inscribir_materia(self, nuevaMateria):
        if(self.estoy_inscripto_materia(nuevaMateria)):
            print(f"Alumno ya inscripto")
            return        
        self.materias.append(nuevaMateria)


    def promedio_materia(self, materia):
        notas = self.materias.get(materia, [])
        return sum(notas) / len(notas) if notas else 0

    def promedio_general(self):
        promedios = [self.promedio_materia(m) for m in self.materias if self.materias[m]]
        return sum(promedios) / len(promedios) if promedios else 0

    def condicion(self):
        if not any(self.materias.values()):
            return "SIN NOTAS REGISTRADAS"
        return "APROBADO" if self.promedio_general() >= self.NOTA_APROBACION else "REPROBADO"

    def reporte(self):
        print("\n" + "=" * 50)
        print(f"REPORTE ACADÉMICO - {self.nombre}")
        print("=" * 50)
        print(f"Edad:    {self.edad}")
        print(f"Carrera: {self.carrera}")
        print("-" * 50)
        print("Materias inscriptas:")
        if not self.materias:
            print("  (ninguna)")
        else:
            for materia, notas in self.materias.items():
                if notas:
                    prom = self.promedio_materia(materia)
                    notas_str = ", ".join(str(n) for n in notas)
                    print(f"  - {materia:20s} Notas: [{notas_str}]  Promedio: {prom:.2f}")
                else:
                    print(f"  - {materia:20s} (sin notas)")
        print("-" * 50)
        print(f"Promedio general: {self.promedio_general():.2f}")
        print(f"Condición final:  {self.condicion()}")
        print("=" * 50)