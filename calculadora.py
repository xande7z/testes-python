# 1) criar a classe chamada 'calculadora'

# correspondente do 'this' 
# em Python: self
class Calculadora:

# 2) Criar o metodo chamado 'soma'
    def soma(self, n1, n2):
        return n1 + n2
    
    
# 4) Criando o metodo chamado 'sutração'
    def subtracao(self, n1, n2):
        return n1 - n2
    
    
# 4) Criando o metodo chamado 'multiplicação'
    def multiplicacao(self, n1, n2):
        return n1 * n2
    
    
# 5) Criando o metodo chamado 'disisão'
    def divisao(self, n1, n2):
        if n2 == 0:
            return ('Divisão inválida')
        
        return n1 / n2