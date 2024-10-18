from. veiculo import Veiculo

class Carro(Veiculo):
    lista_de_veiculos = []

    def __init__(self, marca, modelo, ano, valor_diario, tipo_combustivel):
        super().__init__(marca, modelo, ano, valor_diario)
        self.__tipo_combustivel = tipo_combustivel
        Carro.lista_de_veiculos.append(self)

    @property
    def tipo_combustivel(self):
        return self.__tipo_combustivel
    
    @tipo_combustivel.setter
    def tipo_combustivel(self, tipo_combustivel):
        self.__tipo_combustivel = tipo_combustivel

    def calcular_valor_aluguel(self, dias, desconto=0):
        total = super().calcular_valor_aluguel(dias, desconto)
        if dias > 7:
            total = total - (total * (10/100))
            return f"{dias:.0f} {total:.2f}"
        else:
            return f"{dias:.0f} {total:.2f}"
        
    def aplicar_aumento(cls, percentual):
        for veiculo in cls.lista_de_veiculos:
            # Acessando o atributo corretamente via Veiculo
            novo_valor = veiculo._Veiculo__valor_diario + (veiculo._Veiculo__valor_diario * percentual / 100)
            veiculo._Veiculo__valor_diario = novo_valor
        return novo_valor