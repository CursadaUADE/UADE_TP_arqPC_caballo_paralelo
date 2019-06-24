import time
from caballo import Caballo


def recorrer(formato='Simple'):
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
    print()
    print("=========================================")
    print("Proceso finalizado.", tablero_recorrido)
    print("* Cantidad de ejecuciones:", str(cant))
    print("* Tiempo de ejecución:", duracion, "segundos")
    print(caballo.recorrido)
    print()
    print('* hash_b64: ', caballo.recorrido.hash_b64)
    print('* hash: ', caballo.recorrido.hash)
    print("Tiempo de ejecucion| Ejecucion nro | Tiempo por cada ejecucion |")
    print(
        duracion, "|",
        cant, "|",
        duracion / cant, "|",
        caballo.recorrido.hash_b64, "|",
        formato, "|"
    )
    print("=========================================")


def main():
    recorrer('Simple')


if __name__ == '__main__':
    main()
