#  Importar a classe 'Calculadora'
from calculadora import Calculadora

# 2) Importar o pacote de testes unitários 
# chamado 'unittest'
import unittest

# 3) Criando a classe de testes unitários
class TestCalculadora(unittest.TestCase):

    # Criando o objeto que herdará a classe 'calculadora' 

    # OBS: é necessario usar o método chamado 'setUp'
    def setUp(self):
        self.calc = Calculadora()
        
    # 5) Criar o método de teste
    # do método 'soma()'
    def testSoma(self):
        self.assertEqual(self.calc.soma(2, 3), 5, 'Deve somar dois números')
        self.assertEqual(self.calc.soma(20, 10), 30, 'Deve somar dois números')
        self.assertEqual(self.calc.soma(4500, 2003), 6503, 'Deve somar dois números')

    # Criando o metodo de teste 'subtrção()
    def testSubtracao(self):
        self.assertEqual(self.calc.subtracao(10, 5), 5, 'Deve subtrair dois números')

    # Criando o metodo de teste 'multiplicação()
    def testMultiplicacao(self):
        self.assertEqual(self.calc.multiplicacao(5, 5), 25, 'Deve multiplicar dois números')

    # Criando o metodo de teste 'divisão()
    def testDivisao(self):
        self.assertEqual(self.calc.divisao(12, 3), 4, 'Deve divdir dois números')

# 5) Criando o método de teste
# para uma divisão por zero
    def test_divisao_por_zero(self):
            self.assertEqual(self.calc.divisao(1, 0), 'Divisão inválida')

# Executar a classe de testes unitários
if __name__ == '__main__':
    unittest.main()
    