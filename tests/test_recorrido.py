from unittest import TestCase

from ..recorrido import Recorrido


class TestsRecorrido(TestCase):

    def setUp(self):
        self.recorrido = Recorrido()

    def test_agregar_posicion(self):
        self.recorrido.agregar_posicion((1, 1))
        assert self.recorrido.posiciones_recorridos == [(1, 1)]

    def test_obtener_posiciones_disponibles_descartar_usados(self):
        self.recorrido.agregar_posicion((1, 1))
        self.recorrido.agregar_posicion((1, 2))
        posiciones_posibles = [(1, 1), (1, 2), (3, 1)]
        result = self.recorrido.obtener_posiciones_disponibles(
            posiciones_posibles
        )
        assert result == [(3, 1)]

    def test_obtener_posiciones_disponibles_descartar_fuera_de_rango(self):
        self.recorrido.agregar_posicion((1, 1))
        self.recorrido.agregar_posicion((1, 2))
        posiciones_posibles = [(2, 2), (9, 2)]
        result = self.recorrido.obtener_posiciones_disponibles(
            posiciones_posibles
        )
        assert result == [(2, 2)]

    def test_cantidad_de_pasos(self):
        assert self.recorrido.cantidad_de_paso == 63

    def test_hash(self):
        mock_hash = [
            '01001111', '01010011', '11001101', '10100001',
            '10001100', '00101011', '10101010', '00001100',
            '00000011', '01010100', '10111011', '01011111',
            '10011010', '00111110', '11001011', '11100101',
            '11101101', '00010010', '10101011', '01001101',
            '10001110', '00010001', '10111010', '10000111',
            '00111100', '00101111', '00010001', '00010110',
            '00010010', '00000010', '10111001', '01000101'
        ]
        assert self.recorrido.hash == mock_hash

    def test_hash_b64(self):
        mock_hash = b'T1PNoYwrqgwDVLtfmj7L5e0Sq02OEbqHPC8RFhICuUU='
        assert self.recorrido.hash_b64 == mock_hash
