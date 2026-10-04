import unittest

from app import calcular


class TestCalculadora(unittest.TestCase):
    def test_soma(self):
        self.assertEqual(calcular(2, 3, "somar"), 5)

    def test_subtracao(self):
        self.assertEqual(calcular(8, 3, "subtrair"), 5)

    def test_multiplicacao(self):
        self.assertEqual(calcular(4, 3, "multiplicar"), 12)

    def test_divisao(self):
        self.assertEqual(calcular(10, 2, "dividir"), 5)

    def test_divisao_por_zero(self):
        with self.assertRaises(ValueError):
            calcular(10, 0, "dividir")

    def test_operacao_invalida(self):
        with self.assertRaises(ValueError):
            calcular(2, 3, "invalida")


if __name__ == "__main__":
    unittest.main()