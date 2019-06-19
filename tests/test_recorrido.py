from ..recorrido import Recorrido


class TestsRecorrido():

    recorrido = Recorrido()

    def test_type_posiciones(self):
        assert type(self.recorrido.posiciones_recorridos) == list

    def test_posiciones_lista_vacia(self):
        assert self.recorrido.posiciones_recorridos == []

    def test_agregar_posicion(self):
        self.recorrido.agregar_posicion((1, 1))
        assert self.recorrido.posiciones_recorridos == [(1, 1)]

    def test_obtener_posiciones_disponibles_descartar_usados(self):
        self.recorrido.posiciones_recorridos = [(1, 1), (1, 2)]
        posiciones_posibles = [(1, 1), (1, 2), (3, 1)]
        result = self.recorrido.obtener_posiciones_disponibles(
            posiciones_posibles
        )
        assert result == [(3, 1)]

    def test_obtener_posiciones_disponibles_descartar_fuera_de_rango(self):
        self.recorrido.posiciones_recorridos = [(1, 1), (1, 2)]
        posiciones_posibles = [(2, 2), (9, 2)]
        result = self.recorrido.obtener_posiciones_disponibles(
            posiciones_posibles
        )
        assert result == [(2, 2)]
