# While com menu de interação para definir cada ação

opcao = -1

while opcao != 0:
    print('''
1 - Cadastrar veículo
2 - Excluir cadastro de veículo
3 - Listar clientes
4 - Registrar entrada
5 - Registrar saída
6 - Editar veículo
7 - Consultar estadias de veículo
''')
    try:
        opcao = int(input("Sua opção: "))
    except:
        print("Digite um número inteiro equivalente a opção escolhida.")
    if opcao == 1:
        cadastrar_veiculo()
    elif opcao == 2:
        excluir_veiculo()
    elif opcao == 3:
        listar_clientes()
    elif opcao == 4:
        registrar_entrada()
    elif opcao == 5:
        registrar_saida()
    elif opcao == 6:
        editar_veiculo()
    elif opcao == 7:
        consultar_estadias()
    else:
        print("Opção inválida.")