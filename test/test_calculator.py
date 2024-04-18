import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from calculator import calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = calculator()
    
    def test_divisao_tipo_int(self):
        self.assertEqual(self.calculator.divisao(10, 10), 1)
        self.assertNotEqual(self.calculator.divisao(10, 5), 3)

    def test_divisao_tipo_float(self):
        self.assertNotEqual(self.calculator.divisao(9.4, 5.5), 51.7)
        self.assertEqual(self.calculator.divisao(10.5, 1.5), 7)
        
    def test_divisao_tipo_string(self):
        with self.assertRaises(TypeError):
            self.calculator.divisao(2, '3')

    def test_divisao_por_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.calculator.divisao(10, 0)
            
    def test_add(self):
        self.assertEqual(self.calculator.add(3, 4), 7)
        self.assertEqual(self.calculator.add(-3, 4), 1)
        self.assertEqual(self.calculator.add(0, 0), 0)
        self.assertEqual(self.calculator.add(3.5, 2.5), 6.0)
        # self.assertEqual(self.calculator.add("3.5",2), 5.5) gera erro, por não ser do tipo inteiro ou float. função implementada dentro da class
     
    def test_subtracao(self):
        self.assertEqual(self.calculator.subtracao(5, 3), 2)
        self.assertEqual(self.calculator.subtracao(-5, -3), -2)
        self.assertEqual(self.calculator.subtracao(5, -3), 8)
        self.assertEqual(self.calculator.subtracao(5.5, 2.5), 3.0) 

        #Não é preciso lançar erros ou fazer testes com soma de strings, pois na class calculator,
        # já há uma função implementada para gerar erro caso não seja float ou inteiro.
if __name__ == "__main__":
    unittest.main()    