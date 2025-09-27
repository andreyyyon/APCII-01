"""
    {Python} class Veiculo
    Classe principal para representar um veículo em um estacionamento.

    @propertys
    String Private - placa      Chave primaria do veículo
    String Private - modelo     Modelo  do veículo
    String Private - cor        Cor do veículo
    String Private - vaga       Vaga que o veículo está ocupando
"""

class Veiculo():
    def __init__(self, placa, modelo, cor, vaga):
        self._validProp("placa", placa)
        self._validProp("modelo", modelo)
        self._validProp("cor", cor)
        self._validProp("vaga", vaga)

        self._placa = placa
        self._modelo = modelo
        self._cor = cor
        self._vaga = vaga

    # Método generico para validação inicial das propriedades
    def _validProp(self, nome_propriedade, valor):
        if not valor or str(valor).strip() == "":
            raise ValueError(f"O campo '{nome_propriedade}' é obrigatório e não pode ser vazio.")
        
        if nome_propriedade == "placa" and len(valor) == 7:
            raise ValueError(f"A placa {valor} informada está inválido. Uma placa deve ter exatamente 7 caracteres (ex: ABC1D23).")

    # Método para limpar a propriedade vaga
    def limpaVaga(self):
        self._vaga = ""

    @property
    def placa(self):
        return self._placa

    @placa.setter
    def placa(self, placa):
            self._validProp("placa", placa)
            self._placa = placa

    @property
    def modelo(self):
        return self._modelo

    @modelo.setter
    def modelo(self, modelo):
            self._validProp("modelo", modelo)
            self._modelo = modelo

    @property
    def cor(self):
        return self._cor

    @cor.setter
    def cor(self, cor):
            self._validProp("cor", cor)
            self._cor = cor

    @property
    def vaga(self):
        return self._vaga

    @vaga.setter
    def vaga(self, vaga):
            self._validProp("vaga", vaga)
            self._vaga = vaga


"""
    {Python} class Carro
    Subclasse que representa um carro.

    @propertys
    String Private - tamanho    Porte do veículo (M ou G)
"""

class Carro(Veiculo):    
    def __init__(self, placa, modelo, cor, vaga, tamanho):
        super().__init__(placa, modelo, cor, vaga)
        
        self._validProp("tamanho", tamanho)
        self._validTamanho("tamanho", tamanho)
        self._tamanho = tamanho

    # Método generico para validação inicial das propriedades
    def _validTamanho(self, nome_propriedade, valor):   
        if nome_propriedade == "tamanho" and (valor != "M" and valor != "G"):
            raise ValueError(f"O porte do veículo precisa ser 'M' ou 'G'.")



    @property
    def tamanho(self):
        return self._tamanho

    @tamanho.setter
    def tamanho(self, novo_tamanho):
        self._tamanho = novo_tamanho

"""
    {Python} class Moto
    Subclasse que representa uma moto.

    @propertys
    String Boolean - eletrica   Moto é elétrica? (True - Sim / False - Não)
"""

class Moto(Veiculo):    
    def __init__(self, placa, modelo, cor, vaga, eletrica):
        super().__init__(placa, modelo, cor, vaga)
        
        self._eletrica = eletrica

    @property
    def eletrica(self):
        return self._eletrica

    @eletrica.setter
    def eletrica(self, eletrica):
        self._eletrica = eletrica

"""
    {Python} class Estadia
    Classe principal para representar as estadias em um estacionamento.

    @propertys
    String Private - vaga        Vaga utilizada	
    String Private - placa       Placa do carro que utilizou a vaga		
    String Private - entrada     Data e hora da entrada
    String Private - saida       Data e hora da saida
"""

class Estadia():
    def __init__(self, vaga, placa, entrada, saida):
        self._vaga = vaga
        self._placa = placa
        self._entrada = entrada
        self._saida = saida
    
    @property
    def vaga(self):
        return self._vaga

    @vaga.setter
    def vaga(self, vaga):
            self._vaga = vaga

    @property
    def placa(self):
        return self._placa

    @placa.setter
    def placa(self, placa):
            self._placa = placa

    @property
    def entrada(self):
        return self._entrada

    @entrada.setter
    def entrada(self, entrada):
            self._entrada = entrada
    
    @property
    def saida(self):
        return self._saida

    @entrada.setter
    def saida(self, saida):
            self._saida = saida
