from _classes import Carro, Moto, cliente

from datetime import datetime
import pytz

# Funções

def registrar_entrada(clientes):
    try:
        fuso_brasilia = pytz.timezone("America/Sao_Paulo")
        placa = str(input("Digite a placa do veículo: ")) #id do cliente
        hora = datetime.now(fuso_brasilia)

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

        for clientesExistente in clientes:
            # se já existir o cliente, registra a entrada
            if placa == clientesExistente.placa:
                print("Cadastro já existente, fazendo o registro da entrada...")
                if tipo_veiculo == "Carro":
                    objeto = 

                return

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
    if not clientes:
        print(f"Nenhum veículo cadastrado ainda.")

    placa_buscar = input("Insira a placa do veículo que deseja editar"):

    # Buscar o veículo
    for cliente in clientes:
        if cliente.placa == placa_buscar:
            print(f"\nEditando o veículo: {clientes.modelo} - Placa: {cliente.placa}")

        # Editar o modelo
        nova_cor = input()

def consultar_estadias(estadias):
    pass

    except TypeError as e:
        print(f"Erro: {e}")
    