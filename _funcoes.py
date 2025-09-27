from datetime import datetime
import pytz
from _classes import Veiculo, Carro, Moto, Estadia
import _dados

# Funções

def registrar_entrada(clientes):
    try:
        # Atributo hora/data
        fuso_brasilia = pytz.timezone("America/Sao_Paulo")
        hora = datetime.now(fuso_brasilia)

        # Definindo os atributos da classe Veiculo
        placa = str(input("Digite a placa do veículo: ")) #id do cliente
        modelo = str(input("Qual o modelo do veículo? ")).strip()
        cor = str(input("Qual cor? ")).strip()

        # Definindo os atributos da subclasse
        tipo_veiculo = str(input("Qual o tipo do veículo? [Carro/Moto] ")).strip().capitalize()
        if tipo_veiculo != "Carro" and tipo_veiculo != "Moto":
            print("Tipo de veículo não atendido pelo estacionamento.")
        elif tipo_veiculo == "Carro":
            tam_carro = str(input("Qual o tamanho do carro? [M/G] ")).strip().upper()
        elif tipo_veiculo == "Moto":
            eletrica = str(input("A moto é elétrica? [S/N] ")).strip().upper()
            if eletrica == "S":
                eletrica = True
            elif eletrica == "N":
                eletrica = False
            else:
                print("Digite S ou N")

        # Definindo a vaga
        if tipo_veiculo == "Carro":
            if tam_carro == "M":
                for vagaPretendida in _dados.vagas:
                    if vagaPretendida[0] == "M":
                        vaga = vagaPretendida
                        _dados.vagas.remove(vagaPretendida)
            elif tam_carro == "G":
                for vagaPretendida in _dados.vagas:
                    if vagaPretendida[0] == "G":
                        vaga = vagaPretendida
                        _dados.vagas.remove(vagaPretendida)

        elif tipo_veiculo == "Moto":
            if eletrica == True:
                for vagaPretendida in _dados.vagas:
                    if vagaPretendida[0] == "E":
                        vaga = vagaPretendida
                        _dados.vagas.remove(vagaPretendida)

            elif eletrica == False:
                for vagaPretendida in _dados.vagas:
                    if vagaPretendida[0] == "C":
                        vaga = vagaPretendida
                        _dados.vagas.remove(vagaPretendida)
                
        # Verifico se o cliente ja existe na lista de clientes.
        for clientesExistente in _dados.clientes:
            # se já existir o cliente, registra a entrada
            if placa == clientesExistente.placa:
                print("Cadastro já existente, fazendo o registro da entrada...")
                estadiaNova = Estadia(placa, modelo, hora)
                _dados.estadias.append(estadiaNova)
                return
        
        # Caso não exista, vamos registrar o cliente e em seguida registrar a entrada.
        if tipo_veiculo == "Carro":
            clienteNovo = Carro(placa, modelo, cor, vaga, tam_carro)
            _dados.clientes.append(clienteNovo)
        elif tipo_veiculo == "Moto":
            clienteNovo = Moto(placa, modelo, cor, vaga, eletrica)
            _dados.clientes.append(clienteNovo)

        estadiaNova = Estadia(placa, modelo, hora)
        _dados.estadias.append(estadiaNova)
        return


    except TypeError as e:
        print(f"Erro: {e}")
    