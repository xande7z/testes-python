class CalculadoraIMC:
    def calcular_IMC(self, peso: float, altura: float):
        imc = peso / (altura * altura )
        
        if imc <19:
            return 'magreza'
        
        elif imc >= 19 and imc <24:
            return 'normal'
        
        elif imc >= 24 and imc <29:
            return 'sobrepeso'
        
        else:
            return 'obesidade'
        