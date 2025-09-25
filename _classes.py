"""
    {Python} class Veiculo
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

"""
    {Python} class Carro
    Classe principal para representar um veículo em um estacionamento.

    @propertys
    String Private - portas            Quantidade de portas do veículo carro
"""

class Carro(Veiculo):    
    def __init__(self, placa, modelo, cor, proprietario, portas):
        # Aqui você usa a função super() para chamar o construtor da classe base (Veiculo)
        super().__init__(placa, modelo, cor, proprietario)
        
        # Agora você inicializa os atributos específicos de Carro
        self._portas = portas

    @property
    def portas(self):
        return self._portas

    @portas.setter
    def portas(self, novas_portas):
        self._portas = novas_portas