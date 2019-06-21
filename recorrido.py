import base64
import json
import hashlib


class Recorrido:

    __posiciones_recorridas = None
    __limite = 8
    __hash = None

    def __init__(self):
        self.__posiciones_recorridas = []

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
        h.update(bytes(json.dumps(self.__posiciones_recorridas), 'ascii'))

        return h.digest()

    @property
    def cantidad_de_pasos(self):
        """Devuelve cantidad de pasos recorridos."""
        return len(self.__posiciones_recorridas)

    @property
    def cantidad_maxima_de_pasos(self):
        """Devuelve cantidad maxima de pasos. n**2-1"""
        return self.__limite ** 2

    @property
    def posiciones_recorridas(self):
        return self.__posiciones_recorridas

    def agregar_posicion(self, posicion):
        """agrega posicion a la lista de posiciones"""
        self.__posiciones_recorridas.append(posicion)

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
            lambda x: (x not in self.__posiciones_recorridas),
            posiciones_posibles
        )
        # filtro las posiciones que estan fuera del ranga
        posiciones_disponibles = list(
            filter(
                lambda x: (
                    x[0] in range(self.__limite) and
                    x[1] in range(self.__limite)
                ),
                filtro
            )
        )
        return posiciones_disponibles

    def __str__(self):
        out = ""
        for fila in range(8):
            out += "-----------------------------------------\n"
            for columna in range(8):
                if (fila, columna) in self.__posiciones_recorridas:
                    out += "| {:02d} ".format(
                        self.__posiciones_recorridas.index((fila, columna)) + 1
                    )
                else:
                    out += "|    "

            out += "|\n"

        out += "-----------------------------------------\n"
        out += "Movimientos: " + str(self.cantidad_de_pasos)

        return out
