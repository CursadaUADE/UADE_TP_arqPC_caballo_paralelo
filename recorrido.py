import base64
import json
import hashlib


class Recorrido:

    __posiciones_recorridos = None
    __limite = 8
    __hash = None

    def __init__(self):
        self.__posiciones_recorridos = []

    @property
    def hash(self):
        """Devuelve un hash del recorrido como un array binario."""
        hash_ = []
        for x in self.__get_digesto():
            hash_.append(format(x, '08b'))
        return hash_

    @property
    def hash_b64(self):
        """Devuelve un hash del recorrido en base64."""
        return base64.b64encode(self.__get_digesto())

    def __get_digesto(self):
        """A aprtir de la lista de posiciones recorridos genera un hash"""
        h = hashlib.sha256()
        h.update(bytes(json.dumps(self.__posiciones_recorridos), 'ascii'))
        return h.digest()

    @property
    def cantidad_de_paso(self):
        """Devuelve cantidad maxima de pasos. n**2-1"""
        return (self.__limite ** 2 - 1)

    @property
    def posiciones_recorridos(self):
        return self.__posiciones_recorridos

    def agregar_posicion(self, posicion):
        """agrega posicion a la lista de posiciones"""
        self.__posiciones_recorridos.append(posicion)

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
            lambda x: (x not in self.__posiciones_recorridos),
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
