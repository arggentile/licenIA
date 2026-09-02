"""
Sistema de gestión de tareas para gestionarlas y asignarlas a los empleados para su posterior procesamiento. Las tareas tiene un peso de importancia para poder atender las más urgentes.

tarea

crear, asignar_empleado, asignar_prioridad, eliminar, buscar_tarea, buscar_tarea_asignada_empleado

"""

class tarea:
    def __init__(self, nombre, tipo, empleado, peso):
        self.nombre = nombre
        self.tipo = tipo
        self.empleado = empleado
        self.peso = peso
        self.etiquetas = []

    def asignar_empleado(self, empleado):
        self.empleado = empleado

    def asignar_prioridad(self, prioridad):
        self.prioridad = prioridad

    def asignar_prioridad(self, prioridad):
        self.prioridad = prioridad
