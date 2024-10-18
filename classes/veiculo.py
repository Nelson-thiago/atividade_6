class Veiculo:
    total_veiculos = 0

    def __init__(self, tipo_veiculo, marca, modelo, ano, valor_diario,):
        self.__tipo_veiculo = tipo_veiculo
        self.__marca = marca
        self.__modelo = modelo
        self.__ano = ano
        self.__valor_diario = valor_diario
        Veiculo.total_veiculos += 1

    @property
    def tipo_veiculo(self):
        return self.__tipo_veiculo

    @tipo_veiculo.setter
    def tipo_veiculo(self, tipo_veiculo):
        self.__tipo_veiculo = tipo_veiculo

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

    # Método para ser sobrescrito nas subclasses
    def verifica_tipo_veiculo(self):
        return "Tipo de veículo desconhecido"

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
        return f'{self.marca} {self.modelo} {self.ano} {self.valor_diario}'