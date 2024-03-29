import random
from recorrido import Recorrido


class Caballo:

    __posicion_actual = None
    __recorrido = None
    __movimientos_disponibles = (
        (-1, -2), (-1, 2), (1, -2), (1, 2),
        (-2, -1), (2, -1), (-2, 1), (2, 1),
    )
    __posiciones_posibles = None

    def __init__(self, posicion_inicial):
        self.__recorrido = Recorrido()
        self.__posiciones_posibles = []
        self.mover(posicion_inicial)

    @property
    def recorrido(self):
        return self.__recorrido

    @property
    def tablero_completado(self):
        return self.__recorrido.cantidad_maxima_de_pasos == len(
            self.__recorrido.posiciones_recorridas
        )

    @property
    def cantidad_de_pasos(self):
        return self.__recorrido.cantidad_de_pasos

    @property
    def posiciones_recorridas(self):
        return self.__recorrido.posiciones_recorridas

    def mover(self, posicion):
        self.__posicion_actual = posicion
        self.__recorrido.agregar_posicion(self.__posicion_actual)
        self.__actualizar_posiciones_posibles(self.__posicion_actual)

    def recorrer_tablero(self):
        posiciones = self.__recorrido.obtener_posiciones_disponibles(
            self.__posiciones_posibles
        )

        while posiciones:
            self.__mover_a_posicion_random(posiciones)
            posiciones = self.__recorrido.obtener_posiciones_disponibles(
                self.__posiciones_posibles
            )

    def __mover_a_posicion_random(self, posiciones_posibles):
        nueva_posicion = random.choice(posiciones_posibles)
        self.mover(nueva_posicion)

    def __actualizar_posiciones_posibles(self, posicion_nueva):
        self.__posiciones_posibles = []
        for mov in self.__movimientos_disponibles:
            self.__posiciones_posibles.append((
                posicion_nueva[0] + mov[0],
                posicion_nueva[1] + mov[1]
            ))

    def __str__(self):
        """
        ---------------------------------
        | c | c | c | c | c | c | c | c |
        ---------------------------------
        | c | c | c | c | c | c | c | c |
        ---------------------------------
        | c | c | c | c | c | c | c | c |
        ---------------------------------
        | c | c | c | c | c | c | c | c |
        ---------------------------------
        | c | c | c | c | c | c | c | c |
        ---------------------------------
        | c | c | c | c | c | c | c | c |
        ---------------------------------
        | c | c | c | c | c | c | c | c |
        ---------------------------------
        | c | c | c | c | c | c | c | c |
        ---------------------------------
        """
        out = ""
        for fila in range(8):
            out += "---------------------------------\n"
            for columna in range(8):
                if (fila, columna) in self.__posiciones_posibles:
                    out += "| P "
                elif (fila, columna) == self.__posicion_actual:
                    out += "| C "
                else:
                    out += "|   "

            out += "|\n"

        out += "---------------------------------"

        return out
