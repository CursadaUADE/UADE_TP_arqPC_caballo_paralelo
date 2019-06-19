class Recorrido:

    posiciones_recorridos = None
    __hash = None
    __limite = 8

    @property
    def hash(self):
        return self.__hash

    def __init__(self):
        self.posiciones_recorridos = []

    def agregar_posicion(self, posicion):
        """agrega posicion a la lista de posiciones"""
        self.posiciones_recorridos.append(posicion)

    def obtener_posiciones_disponibles(self, posiciones_posibles):
        """Apartir de la lista de posiciones recibidas
        devuelve un listado de posiciones disponibles.

        Parametros:
            posiciones_posibles: lista
                lista de posiciones posibles.
        Respuesta
            lista de posiciones disponibles.
        """

        # de la lista recibida filtro las posiciones usadas.
        filtro = filter(
            lambda x: (x not in self.posiciones_recorridos),
            posiciones_posibles
        )
        # filtro las posiciones que estan fuera del ranga
        posiciones_disponibles = list(
            filter(
                lambda x: not (x[0] > self.__limite or x[1] > self.__limite),
                filtro
            )
        )
        return posiciones_disponibles
