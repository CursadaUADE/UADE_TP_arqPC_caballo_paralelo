"""
caballo_recorrido.py

Problema del Caballo - Programa principal
"""

import time
from caballo import Caballo


def recorrer(formato='Simple'):
    """
    Función de recorrido. Inicializa un caballo y lo hace correr hasta que
    logra completar un recorrido.

    Args:
        recorrer: str
    """
    print("Inicio de la corrida.", formato)
    tablero_recorrido = False
    cant = 0

    inicio = time.time()
    while not tablero_recorrido:
        caballo = Caballo((0, 0))
        caballo.recorrer_tablero()
        cant += 1
        tablero_recorrido = caballo.tablero_completado

    duracion = time.time() - inicio
    print()
    print("Proceso finalizado.", tablero_recorrido)
    print(caballo.recorrido)
    print()
    print("Tiempo de ejecución", end=",")
    print("Cant. de ejecuciones", end=",")
    print("Tiempo por cada ejecución", end=",")
    print("Hash", end=",")
    print("Formato")
    print(
        duracion, ",",
        cant, ",",
        duracion / cant, ",",
        caballo.recorrido.hash_b64, ",",
        formato, ","
    )


def main():
    recorrer('Simple')


if __name__ == '__main__':
    main()
