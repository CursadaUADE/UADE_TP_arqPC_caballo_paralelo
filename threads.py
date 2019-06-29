"""
threads.py

Problema del Caballo - Implementación con Threads.
"""

import threading
import caballo_recorrido


def main():
    threads = []
    for _ in range(4):
        thread = threading.Thread(
            target=caballo_recorrido.recorrer, args=('Thread',)
        )
        threads.append(thread)
        thread.start()

    for _ in threads:
        thread.join()


if __name__ == '__main__':
    main()
