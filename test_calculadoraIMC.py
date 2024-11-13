from calculadoraIMC import CalculadoraIMC

import unittest

class testCalculadoraIMC(unittest.TestCase):
    def setUp(self):
        self.calc = CalculadoraIMC()
        
    def testImc_magreza(self):
        self.assertEqual(self.calc.calcular_IMC(50, 1.80), 'magreza')
        

if __name__ == '__main__':
    unittest.main()