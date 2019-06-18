class Caballo:

    __posicion_actual = None

    def __init__(self):
        self.__posicion_actual = (0, 0)

    def mover(self, posicion):
        pass

    @property
    def posiciones_posibles(self):
        pass

    def recorrer_tablero(self):
        pass


class Recorrido:

    posiciones = None
    __hash = None

    @property
    def hash(self):
        return self.__hash

    def __init__(self):
        self.posiciones = []

    def agregar_posicion(posicion):
        """agrega posicion a la lista de posiciones"""
        pass

    def obtener_posiciones_disponibles(self, posiciones_posibles):
        pass
