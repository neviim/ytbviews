
import unittest

def soma(parcela1, parcela2):
    return parcela1 + parcela2


class CanaisTests(unittest.TestCase):
    def test_soma(self):
        resultado = soma(1, 2)
        self.assertEquals(3, resultado)

    def test_nada(self):
        pass