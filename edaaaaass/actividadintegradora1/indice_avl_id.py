from arbol_avl import ArbolAvl
from event import Event


class IndiceAvlId:
    """
    Indice de eventos por id_evento, basado en un arbol AVL. (nos apoyamos en la implementacion de ArbolAvl )

    A diferencia del Index basado en diccionario (hash) — que da acceso O(1)
    pero sin orden —, este indice AVL mantiene las claves ordenadas y balanceadas,
    lo que habilita consultas que el hash no puede responder eficientemente:

      - buscar por id exacto      -> O(log n)
      - rango de ids [min, max]   -> O(log n + k)
      - recorrido ordenado por id -> O(n)
      - id minimo / id maximo     -> O(log n)

    Como los id_evento son unicos (clave primaria del evento), cada nodo del AVL
    guarda un unico Event (no una lista como en el indice temporal).
    """

    def __init__(self):
        self._arbol = ArbolAvl()
        self._cantidad = 0

    def agregar_evento(self, evento: Event):
        """
        Inserta un evento indexado por su id_evento.
        Si el id ya existe, produce una excepcion.
        O(log n).
        """
        if not isinstance(evento, Event):
            raise TypeError("Se esperaba una instancia de Event.")

        if not isinstance(evento, Event):
            raise TypeError("Se esperaba una instancia de Event.")

        if not self._arbol.contiene(evento.id_evento):
            self._cantidad += 1
            self._arbol.insertar(evento.id_evento, evento)
        else:
            raise ValueError("El id_evento ya existe en el indice.")

    def buscar(self, id_evento):
        """
        Devuelve el Event con el id indicado, o None si no existe.
        O(log n).
        """
        return self._arbol.buscar(id_evento)

    def contiene(self, id_evento):
        """ Verifica si existe un evento con ese id. O(log n). """
        return self._arbol.contiene(id_evento)

    def eventos_en_rango(self, id_min, id_max):
        """
        Devuelve todos los eventos cuyo id_evento este en [id_min, id_max],
        ordenados ascendentemente por id.
        O(log n + k).
        """
        rango = self._arbol.rango(id_min, id_max)
        return [evento for _, evento in rango]

    def listar_ordenado(self):
        """
        Devuelve todos los eventos ordenados ascendentemente por id_evento
        (recorrido in-orden del AVL).
        O(n).
        """
        return [evento for _, evento in self._arbol.inorden()]

    def cantidad(self):
        return self._cantidad

    def altura(self):
        return self._arbol.altura_arbol()


if __name__ == "__main__":
    eventos = []
    eventos.append( Event(614827, "2026-03-05T08:22:15Z",  "EMERGENCIA MEDICA", 2, "Adulto mayor con dolor toracico intenso", "B", "C"))
    eventos.append( Event(738201, "2026-03-07T19:45:33Z",  "ROBO", 4, "Hurto de motocicleta en estacionamiento", "C", "E"))
    eventos.append( Event(205544, "2026-03-18T02:08:17Z",  "EMERGENCIA MEDICA", 4, "Intoxicacion alcoholica en joven", "E", "A"))
    eventos.append( Event(391877, "2026-06-22T11:33:40Z",  "ROBO", 2, "Entradera a vivienda", "D", "B"))
    eventos.append( Event(582039, "2026-04-14T17:55:12Z",  "EMERGENCIA MEDICA", 3, "Caida de obrero desde andamio", "C", "D"))
    eventos.append( Event(946715, "2026-07-30T23:41:08Z",  "EMERGENCIA MEDICA", 1, "Parto en domicilio", "B", "A"))
    eventos.append( Event(417206, "2026-02-14T09:12:44Z",  "Accidente de Transito", 2, "Colision frontal", "E", "C"))
    eventos.append( Event(853990, "2026-02-14T13:28:19Z",  "Disturbio", 4, "Pelea entre hinchas", "A", "B"))
    eventos.append( Event(672188, "2026-02-14T18:04:55Z",  "EMERGENCIA MEDICA", 4, "Reaccion alergica severa", "C", "D"))
    eventos.append( Event(239074, "2026-02-14T21:50:31Z",  "Accidente de Transito", 2, "Motociclista derrapo", "B", "E"))
    eventos.append( Event(508623, "2026-02-14T23:17:02Z",  "EMERGENCIA MEDICA", 2, "Incendio en departamento", "D", "C"))
    eventos.append( Event(760451, "2026-02-14T04:36:28Z",  "Disturbio", 3, "Ruidos molestos", "E", "B"))

    indice = IndiceAvlId()
    for evento in eventos:
        indice.agregar_evento(evento)

    print(f"Cantidad de eventos: {indice.cantidad()}")
    print(f"Altura del arbol: {indice.altura()}")

    print("\n--- Busqueda por id exacto ---")
    evento_buscado = indice.buscar(508623)
    print(f"id=508623 -> {evento_buscado.info() if evento_buscado else 'No encontrado'}")

    evento_buscado = indice.buscar(672188)
    print(f"id=672188 -> {evento_buscado.info() if evento_buscado else 'No encontrado'}")

    evento_buscado = indice.buscar(11)
    print(f"id=11  -> {evento_buscado.info() if evento_buscado else 'No encontrado'}")

    
    print("\n--- Eventos con id entre 400000 y 700000 (ordenados ascendentemente) ---")
    print(f"{'ID':<8}{'FECHA':<22}{'TIPO':<22}{'PRIO':<6}{'DESCRIPCION':<55}{'O':<4}{'D':<4}")
    print("-" * 121)
    for e in indice.eventos_en_rango(400000, 700000):
        print(e.info())
  
    print("\n--- Todos los eventos ordenados por id (in-orden del AVL) ---")
    for e in indice.listar_ordenado():
        print(f"  id={e.id_evento}  {e.timestamp}  {e.categoria}")