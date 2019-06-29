"""
processes.py

Problema del Caballo - Implementación con Procesos.
"""

import caballo_recorrido
import multiprocessing


def main():
    for i in range(multiprocessing.cpu_count()):
        process = multiprocessing.Process(
            name='Process: {}'.format(i),
            target=caballo_recorrido.recorrer,
            args=('Process',)
        )
        process.start()


if __name__ == '__main__':
    main()
