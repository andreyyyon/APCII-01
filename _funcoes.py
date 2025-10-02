import os
import platform
import pytz
import _dados
from datetime import datetime
from _classes import Carro, Moto, Estadia

# # Funções

def registrar_entrada():
    try:
        # Atributo hora/data
        fuso_brasilia = pytz.timezone("America/Sao_Paulo")
        hora = datetime.now(fuso_brasilia)

        # Definindo os atributos da classe Veiculo
        placa = str(input("Digite a placa do veículo: ")) #id do cliente
        modelo = str(input("Qual o modelo do veículo? ")).strip()
        cor = str(input("Qual cor? ")).strip()

        # Definindo os atributos da subclasse
        tipo_veiculo = str(input("Qual o tipo do veículo? [Carro/Moto] ")).strip()[0].upper()
        if tipo_veiculo != "C" and tipo_veiculo != "M":
            print("Tipo de veículo não atendido pelo estacionamento.")
        elif tipo_veiculo == "C":
            tam_carro = str(input("Qual o tamanho do carro? [M/G] ")).strip().upper()
        elif tipo_veiculo == "M":
            eletrica = str(input("A moto é elétrica? [S/N] ")).strip().upper()
            if eletrica == "S":
                eletrica = True
            elif eletrica == "N":
                eletrica = False
            else:
                print("Digite S ou N")

        # Definindo a vaga
        if tipo_veiculo == "C":
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

        elif tipo_veiculo == "M":
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
                estadiaNova = Estadia(vaga, placa, hora, None)
                _dados.estadias.append(estadiaNova)
                pass
        
        # Caso não exista, vamos registrar o cliente e em seguida registrar a entrada.
        try:
            if tipo_veiculo == "C":
                clienteNovo = Carro(placa, modelo, cor, vaga, tam_carro)
                _dados.clientes.append(clienteNovo)
            elif tipo_veiculo == "M":
                clienteNovo = Moto(placa, modelo, cor, vaga, eletrica)
                _dados.clientes.append(clienteNovo)
        except ValueError as erro_validacao:
            print(f"Erro: {erro_validacao}.")

        estadiaNova = Estadia(vaga, placa, hora, None)
        _dados.estadias.append(estadiaNova)
        print("Entrada registrada com sucesso.")
        return
    
    except TypeError as e:
        print(f"Erro: {e}")
    
def registrar_saida():
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
                pass

        # Adicionar a vaga novamente à lista vagas
        for cliente in _dados.clientes:
            if placa == cliente.placa:
                _dados.vagas.append(cliente.vaga)
                # Remover a vaga da instância da subclasse de Veiculo
                cliente.vaga = None
                print("Saída registrada com sucesso.")
                return 
            
        print("Não foi encontrada estadia em aberto para essa placa.")
    except TypeError as e:
            print(f"Erro: {e}")

# Função para mostrar todos os veículos cadastrados no sistema     
def listar_clientes():
    clientes = _dados.clientes
    if not clientes:
        print("Nenhum veículo cadastrado ainda.")
        return
    
    print("Lista de clientes cadastrados")
    for i, cliente in enumerate(clientes, start=1):
        print(f"{i} - Placa: {cliente.placa}")
        print(f"    - Modelo: {cliente.modelo}")
        print(f"    - Cor: {cliente.cor}")
        print(f"    - Vaga: {cliente.vaga}")

        # Verifica se o objeto pertence a classe correta
        if isinstance(cliente, Carro):
            print(f"    - Tipo: Carro")
            print(f"    - Tamanho: {cliente.tamanho}")

        elif isinstance(cliente, Moto):
            print(f"   Tipo: Moto")
            print(f"   Motor: {'Elétrica' if cliente.eletrica else 'Combustão'}")
            print("-"*40)
        

def editar_veiculo():
    if not _dados.clientes:
        print(f"Nenhum veículo cadastrado ainda.")
        return
    
    placa_buscar = input("Digite a placa do veículo que deseja editar: ")

    # Buscar o veículo
    for cliente in  _dados.clientes:
        if cliente.placa == placa_buscar:
            print(f"\nEditando o veículo: {cliente.modelo} - Placa: {cliente.placa}")
            clienteTemp = cliente

    alterado = False

    # Editar o modelo
    novo_modelo = input(f"Digite o novo modelo (modelo atual: {clienteTemp.modelo}): ").strip()
    print("Ou digite ENTER para manter o modelo atual.")
    if novo_modelo:
        clienteTemp.modelo = novo_modelo
        alterado = True

    # Editar a cor
    nova_cor = input(f"Digite a nova cor (cor atual: {clienteTemp.cor}): ").strip()
    print("Ou digite ENTER para manter a cor atual.")
    if nova_cor:
        clienteTemp.cor = nova_cor
        alterado = True

    if alterado == True:
        print("Veículo atualizado com sucesso!")
    elif alterado == False:
        print("Nenhuma alteração foi feita.")
        return

    print("Veículo não encontrado.")

def consultar_estadias():
    placa = str(input("Qual placa deseja consultar as estadias? "))
    for estadia in _dados.estadias:
            if estadia.placa == placa:
                print(f"Vaga: {estadia.vaga}")
                print(f"Data/hora de entrada: {estadia.entrada}")
                print(f"Data/hora de saída: {estadia.saida}")

def limpar_terminal():
    sistema_operacional = platform.system()
    
    if sistema_operacional == "Windows":
        os.system('cls')
    else:
        os.system('clear')
