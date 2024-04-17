import unittest
from calculator import calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = calculator()
    
    def test_divisao_tipo_int(self):
        self.assertEquals(self.calculator.divisao(10, 10), 1)
        self.assertNotEquals(self.calculator.divisao(10, 5), 3)

    def test_divisao_tipo_float(self):
        self.assertNotEquals(self.calculator.divisao(9.4, 5.5), 51.7)
        self.assertEquals(self.calculator.divisao(10.5, 1.5), 7)
        
    def test_divisao_tipo_string(self):
        with self.assertRaises(TypeError):
            self.calculator.divisao(2, '3')

    def test_divisao_por_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.calculator.divisao(10, 0)

    #TODO - Implementar Testes para os casos de Adição, Subtração e Multiplicação