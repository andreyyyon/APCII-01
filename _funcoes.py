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
            


    except TypeError as e:
        print(f"Erro: {e}")
    