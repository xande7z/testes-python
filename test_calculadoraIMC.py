from calculadoraIMC import CalculadoraIMC

import unittest

class testCalculadoraIMC(unittest.TestCase):
    def setUp(self):
        self.calc = CalculadoraIMC()
        
    def testImc_magreza(self):
        self.assertEqual(self.calc.calcular_IMC(50, 1.80), 'magreza')
        
    def testImc_normal(self):
        self.assertEqual(self.calc.calcular_IMC(60, 1.60), 'normal')
        
    def testImc_sobrepeso(self):
        self.assertEqual(self.calc.calcular_IMC(80, 1.60), 'sobrepeso')
        
    def testImc_obesidade(self):
        self.assertEqual(self.calc.calcular_IMC(180, 1.60), 'obesidade')
        
        
        

if __name__ == '__main__':
    unittest.main()