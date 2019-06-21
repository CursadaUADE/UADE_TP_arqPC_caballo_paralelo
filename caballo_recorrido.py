import time
from caballo import Caballo


def main():
    tablero_recorrido = False
    cant = 0

    inicio = time.time()
    # hashes = []
    while not tablero_recorrido:
        caballo = Caballo()
        caballo.recorrer_tablero()
        cant += 1
        if caballo.cantidad_de_pasos == 64:
            print("=========================================")
            print("Ejecución nro: " + str(cant))
            print(caballo.recorrido)
            print("=========================================")
            print()
            # hashes.append(caballo.recorrido.hash_b64)

        tablero_recorrido = caballo.tablero_completado

    fin = time.time()

    print("Proceso finalizado.")
    print("* Cantidad de ejecuciones:", str(cant))
    print("* Tiempo de ejecución:", str(fin - inicio), "segundos")


if __name__ == '__main__':
    main()
