from catapulta.catapulta import Catapulta
import unittest

class TestCatapulta(unittest.TestCase):

    def setUp(self):
        self.catapulta = Catapulta()

    def test_construir_catapulta(self):
        materiales = ['palos', 'gomas', 'tapones']
        self.catapulta.construir(materiales)
        self.assertEqual(self.catapulta.materiales_utilizados, materiales)

    def test_disparar_proyectil(self):
        self.catapulta.construir(['palos', 'gomas'])
        proyectil = self.catapulta.disparar()
        self.assertIsNotNone(proyectil)

    def test_mostrar_materiales(self):
        materiales = ['palos', 'gomas', 'tapones']
        self.catapulta.construir(materiales)
        self.assertEqual(self.catapulta.mostrar_materiales(), materiales)

if __name__ == '__main__':
    unittest.main()