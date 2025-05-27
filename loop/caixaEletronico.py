saldo = 0

while True:
    print("--- Bem vindo ---")
    print("1 - Verificar Saldo")
    print("2 - Depositar Dinheiro")
    print("3 - Sacar Dinheiro")
    print("4 - Sair")

    pergunta = int(input("Qual opção voce deseja: "))
    
    match pergunta:
        case 1:
            print("Seu saldo é: {}" .format(saldo))
        case 2:
            valor = float(input("Qual valor deseja depositar: "))
            
            if (valor > 0):
                saldo += valor
                
                print("Foi depositado um valor de : {}" .format(valor))
                print("Seu saldo é: {}" .format(saldo))
            else:
                print("O deposito não pode ser negativo!")
                continue
        case 3:
            saque = float(input("Qual valor deseja sacar: "))
            
            if (saque > 0 and saque <= saldo):
                saldo = saldo - saque
                
                print("Foi sacado um valor de : {}" .format(saque))
                print("Seu saldo é: {}" .format(saldo))
            else:
                print("Saque inválido ou saldo insuficiente!")
                continue
        case 4:
            print("Saindo...")
            break
        case _:
            print("Opção inválida!")