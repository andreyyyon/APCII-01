# While com menu de interação para definir cada ação

opcao = -1

while opcao != 0:
    print('''
1 - Registrar entrada
2 - Registrar saída
3 - Listar clientes
4 - Editar veículo
5 - Consultar estadias

0 - Encerrar
          
''')
    try:
        opcao = int(input("Sua opção: "))
    except:
        print("Digite um número inteiro equivalente a opção escolhida.")
    if opcao == 1:
        registrar_entrada()
    elif opcao == 2:
        registrar_saida()
    elif opcao == 3:
        listar_clientes()
    elif opcao == 4:
        editar_veiculo()
    elif opcao == 5:
        consultar_estadias()
    else:
        print("Opção inválida.")