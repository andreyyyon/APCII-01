"""
    {Python} class veiculo
    Classe principal para representar um veículo em um estacionamento.

    @propertys
    String Private - placa            Chave primaria do veículo
    String Private - modelo           Modelo  do veículo
    String Private - cor              Cor do veículo
    String Private - proprietario     Proprietário do veículo
"""

class Veiculo():
    def __init__(self, placa, modelo, cor, proprietario):
        self._placa = placa
        self._modelo = modelo
        self._cor = cor
        self._proprietario = proprietario
    
    @property
    def placa(self):
        return self._placa

    @placa.setter
    def nome(self, placa):
            self._placa = placa

    @property
    def modelo(self):
        return self._modelo

    @modelo.setter
    def modelo(self, modelo):
            self._modelo = modelo

    @property
    def cor(self):
        return self._cor

    @cor.setter
    def cor(self, cor):
            self._cor = cor

    @property
    def proprietario(self):
        return self._proprietario

    @proprietario.setter
    def proprietario(self, proprietario):
            self._proprietario = proprietario