# from _classes import Carro, Moto, cliente

from datetime import datetime
import pytz
from _classes import Veiculo, Carro, Moto, Estadia
import _dados
import os
import platform

# # Funções

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
        try:
            if tipo_veiculo == "Carro":
                clienteNovo = Carro(placa, modelo, cor, vaga, tam_carro)
                _dados.clientes.append(clienteNovo)
            elif tipo_veiculo == "Moto":
                clienteNovo = Moto(placa, modelo, cor, vaga, eletrica)
                _dados.clientes.append(clienteNovo)
        except ValueError as erro_validacao:
            print(f"Erro: {erro_validacao}.")

        estadiaNova = Estadia(placa, modelo, hora)
        _dados.estadias.append(estadiaNova)
        return
    
    except TypeError as e:
        print(f"Erro: {e}")
    
def registrar_saida(clientes):
    try:
        # Atributo hora/data
        fuso_brasilia = pytz.timezone("America/Sao_Paulo")
        hora = datetime.now(fuso_brasilia)

        # Atributo placa do veículo que está saindo
        placa = str(input("Digite a placa do veículo que vai sair: ")).strip()

        # Adicionar horário de saída na instância da classe Estadia que está na lista estadias.
        for estadia in reversed(_dados.estadias):
            if estadia.placa == placa and getattr(estadia, "hora_saida", None) is None:
                estadia.saida = hora
                print(f"Saída registrada para {placa} às {hora.strftime('%d/%m/%Y %H:%M:%S')}")
                return
            
        # Adicionar a vaga novamente à lista vagas

        # Remover a vaga da instância da subclasse de Veiculo
            
        print("Não foi encontrada estadia em aberto para essa placa.")
    except TypeError as e:
            print(f"Erro: {e}")

# Função para mostrar todos os veículos cadastrados no sistema     
def listar_clientes(clientes):
    if not clientes:
        print("Nenhum veículo cadastrado ainda.")
        return
    
    print("Lista de clientes cadastrados")
    for i, clientes in enumerate(clientes, start=1):
        print(f"{i} - Placa: {clientes.placa}")
        print(f"    - Modelo: {clientes.modelo}")
        print(f"    - Cor: {clientes.cor}")
        print(f"    - Vaga: {clientes.vaga}")

# Verifica se o objeto pertence a classe correta
if isinstance(cliente, Carro):
    print(f"    - Tipo: Carro")
    print(f"    - Tamanho: {cliente.tamanho}")

elif isinstance(cliente, Moto):
    print(f"   Tipo: Moto")
    print(f"   Motor: {'Elétrica' if cliente.eletrica else 'Combustão'}")
    print("-"*40)
    
def editar_veiculos(clientes, veiculo):
    pass

def consultar_estadias(estadias):
    pass
    

def limpar_terminal():
    sistema_operacional = platform.system()
    
    if sistema_operacional == "Windows":
        os.system('cls')
    else:
        os.system('clear')
