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
    def placa(self, placa):
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
    Subclasse que vai representar um carro.

    @propertys
    String Private - portas     Quantidade de portas do veículo carro
"""

class Carro(Veiculo):    
    def __init__(self, placa, modelo, cor, proprietario, portas):
        super().__init__(placa, modelo, cor, proprietario)
        
        self._portas = portas

    @property
    def portas(self):
        return self._portas

    @portas.setter
    def portas(self, novas_portas):
        self._portas = novas_portas

"""
    {Python} class Moto
    Subclasse que vai representar uma moto.

    @propertys
"""

class Moto(Veiculo):    
    def __init__(self, placa, modelo, cor, proprietario, x):
        super().__init__(placa, modelo, cor, proprietario)
        
        self._x = x

    @property
    def x(self):
        return self._x

    @x.setter
    def portas(self, x):
        self._x = x

"""
    {Python} class Vaga
    Classe principal para representar uma vaga em um estacionamento.

    @propertys
    String Private - id         Identificador primario da vaga	
    String Private - tipo       Tipo da vaga (C - Carro / M - Moto)		
    String Private - status     Status da vaga (True - Disponivel / False - Ocupada)
"""

class Vaga():
    def __init__(self, id, tipo, status, placaVeiculo):
        self._id = id
        self._tipo = tipo
        self._status = status
        self._placaVeiculo = placaVeiculo
    
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
            self._id = id

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, tipo):
            self._tipo = tipo

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
            self._status = status
