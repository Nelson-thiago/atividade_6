from. veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, nome, marca, modelo, ano, valor_diario, tipo_combustivel):
        super().__init__(nome, marca, modelo, ano, valor_diario)
        self.__tipo_combustivel = tipo_combustivel

    @property
    def tipo_combustivel(self):
        return self.__tipo_combustivel
    
    @tipo_combustivel.setter
    def tipo_combustivel(self, tipo_combustivel):
        self.__tipo_combustivel = tipo_combustivel

    def calcular_valor_aluguel(self, dias, desconto=0):
        total = super().calcular_valor_aluguel(dias, desconto)
        if dias > 7:
            total *= 0.9 # Valor total deduzido os 10%
        return total