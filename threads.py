import threading
import caballo_recorrido


def main():
    lista_thread = []
    for i in range(4):
        thread = threading.Thread(
            target=caballo_recorrido.recorrer, args=('Thread',)
        )
        lista_thread.append(thread)
        print('thread start')
        thread.start()
    for i in lista_thread:
        print('thread.join()')
        thread.join()


if __name__ == '__main__':
    main()
