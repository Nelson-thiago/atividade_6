from .veiculo import Veiculo
class Motocicleta(Veiculo):
    def __init__(self, marca, modelo, ano, valor_diario, cilindrada):
        super().__init__(marca, modelo, ano, valor_diario)  
        self.__cilindrada = cilindrada

    @property
    def cilindrada(self):
        return self.__cilindrada

    @cilindrada.setter
    def cilindrada(self, cilindrada):
        self.__cilindrada = cilindrada

    def calcular_valor_aluguel(self, dias, desconto=None):
        if desconto:
            total = super().calcular_valor_aluguel(dias, desconto)  # Chama o método da classe mãe
        else:
            total = super().calcular_valor_aluguel(dias)
        if self.__cilindrada > 200:  
            total += total * 0.1 
        return total
