from datetime import datetime

class Tarea:
    PRIORIDADES_VALIDAS = ("baja", "media", "alta")

    def __init__(self, descripcion, prioridad="media"):
        self.descripcion = descripcion
        self.prioridad = prioridad # se puede controlar acá
        self.completada = False
        self.fecha_creacion = datetime.now()
       
    def validar_prioridad(self, prioridad):
        prioridad = prioridad.lower()
        if prioridad not in self.PRIORIDADES_VALIDAS:
            print("Prioridad no valida")
            return False           
        return True

    def marcar_completada(self):
        if self.completada:
            print(f"La tarea '{self.descripcion}' ya estaba completada.")
            return False
        self.completada = True
        return True

    def cambiar_prioridad(self, nueva_prioridad):
        if(self.validar_prioridad(nueva_prioridad)):
            self.prioridad = nueva_prioridad
            return True
        else:
            print("no se cambia la prioridad ya que no es valida")

    def esta_pendiente(self):
        return not self.completada
    
    def mostrar_info(self):
        print(f"La tareas con nombre: {self.descripcion} tien estado: {self.estado} creada el {self.fecha_creacion}")
              

class GestorTareas:
    def __init__(self, nombre="Mi lista de tareas"):
        self.nombre = nombre
        self.tareas = []

    def agregar_tarea(self, descripcion, prioridad="media"):
        tarea = Tarea(descripcion, prioridad)
        self.tareas.append(tarea)
        print(f"Tarea agregada exitosamente")
        return tarea
        
    def buscar(self, descripcion):
        for unaTarea in self.tareas:
            if unaTarea.descripcion.lower() == descripcion.lower():
                return unaTarea
        return None

    def cambiar_prioridad(self, descripcion, nueva_prioridad):
        tarea = self.buscar(descripcion)
        if tarea is None:
            print(f"No se encontró la tarea '{descripcion}'.")
            return False
            return tarea.cambiar_prioridad(nueva_prioridad)

    def completar_tarea(self, descripcion):
        tarea = self.buscar(descripcion)
        if tarea is None:
            print(f"No se encontró la tarea '{descripcion}'.")
            return False
        return tarea.marcar_completada()

    def getPendientes(self):
        return [t for t in self.tareas if t.esta_pendiente()]

    def getCompletadas(self):
        return [t for t in self.tareas if t.completada]

    def agrupar_por_prioridad(self, solo_pendientes=False):
        base = self.getPendientes() if solo_pendientes else self.tareas
        grupos = {p: [] for p in Tarea.PRIORIDADES_VALIDAS}
        for t in base:
            grupos[t.prioridad].append(t)
        return grup

    def estadisticas(self):
        total = len(self.tareas)
        completadas = len(self.getCompletadas())
        pendientes = total - completadas
        porcentaje = (completadas / total * 100) if total else 0
        return {
            "total": total,
            "completadas": completadas,
            "pendientes": pendientes,
            "porcentaje_completadas": porcentaje,
        }
    
    def reporte(self):
        print("\n" + "=" * 65)
        print(f"REPORTE - {self.nombre}")
        print("=" * 65)

        stats = self.estadisticas()
        print(f"Total de tareas: {stats['total']}")
        print(f"Completadas:     {stats['completadas']}")
        print(f"Pendientes:      {stats['pendientes']}")
        print(f"Progreso:        {stats['porcentaje_completadas']:.1f}%")
        print("-" * 65)

        print("TAREAS PENDIENTES AGRUPADAS POR PRIORIDAD:")
        grupos = self.agrupar_por_prioridad(solo_pendientes=True)
        # Orden lógico: alta -> media -> baja
        for prioridad in ("alta", "media", "baja"):
            tareas = grupos[prioridad]
            print(f"\n  >> Prioridad {prioridad.upper()} ({len(tareas)}):")
            if not tareas:
                print("     (sin tareas)")
            else:
                for t in tareas:
                    print(f"     - {t.descripcion}  (creada: "
                          f"{t.fecha_creacion.strftime('%d/%m/%Y %H:%M')})")

        print("-" * 65)
        print("TAREAS COMPLETADAS:")
        completadas = self.filtrar_completadas()
        if not completadas:
            print("  (ninguna)")
        else:
            for t in completadas:
                print(f"  ✔ {t.descripcion} ({t.prioridad})")
        print("=" * 65)


gestor = GestorTareas("Tareas de la semana")

    # Crear tareas
gestor.agregar_tarea("Estudiar POO en Python", "alta")
gestor.agregar_tarea("Hacer las compras", "media")
gestor.agregar_tarea("Ordenar el escritorio", "baja")
gestor.agregar_tarea("Entregar TP de programación", "alta")
gestor.agregar_tarea("Responder correos", "media")
gestor.agregar_tarea("Regar las plantas", "baja")
gestor.agregar_tarea("Preparar presentación", "alta")
gestor.agregar_tarea("Tarea inválida", "urgente")  # prioridad inválida

# Simular finalización de algunas 
gestor.completar_tarea("Hacer las compras")
gestor.completar_tarea("Regar las plantas")
gestor.completar_tarea("Responder correos")
gestor.completar_tarea("Hacer las compras")  # ya estaba completada

# Cambiar prioridad de una tarea
gestor.cambiar_prioridad("Ordenar el escritorio", "media")

# Reporte final
gestor.reporte()