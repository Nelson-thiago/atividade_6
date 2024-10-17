class Veiculo:
    total_veiculos = 0

    def __init__(self, marca, modelo, ano, valor_diario):
        self.__marca = marca
        self.__modelo = modelo
        self.__ano = ano
        self.__valor_diario = valor_diario
        Veiculo.total_veiculos += 1

    @property
    def marca(self):
        return self.__marca

    @marca.setter
    def marca(self, marca):
        self.__marca = marca

    @property
    def modelo(self):
        return self.__modelo

    @modelo.setter
    def modelo(self, modelo):
        self.__modelo = modelo

    @property
    def ano(self):
        return self.__ano

    @ano.setter
    def ano(self, ano):
        self.__ano = ano

    @property
    def valor_diario(self):
        return self.__valor_diario

    @valor_diario.setter
    def valor_diario(self, valor_diario):
        self.__valor_diario = valor_diario

    def calcular_valor_aluguel(self, dias, desconto=0):
        total = self.__valor_diario * dias
        total -= total * desconto
        return total

    @classmethod
    def get_total_veiculos(cls):
        return cls.total_veiculos
    
    @classmethod
    def aplicar_aumento(cls, percentual):
        raise NotImplementedError("Implementar nas subclasses")
    
    def __str__(self):
        return f'Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}, Valor diária: {self.valor_diario}'











