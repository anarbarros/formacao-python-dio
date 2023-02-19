menu = '''

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

= > '''


saldo = 0
limite = 500
extrato = " "
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Qual o valor a ser depositado?"))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: r$ {valor:.2f}\n"
        else:
            print("O valor informado é inválido!")
    
    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo
        
        excedeu_limite = valor > limite
        
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Você não tem saldo suficiente!")

        elif excedeu_limite:
            print("O valor do saque excede o limite disponivel !")

        elif excedeu_saques:
            print("Número máximo de saques ao dia!")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: r$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("O valor informado é inválido!")

    elif opcao == "e":
        print("\n========== EXTRATO ==========")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: r$ {saldo:.2f}")
        print("=============================")

    elif opcao == "q":
        break

    else:
        print("Opção inválida, por favor tente novamente!")