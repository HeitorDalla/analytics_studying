listaItens = []

while True:
    print("--- Menu ---")
    print("1. Adicionar item à lista")
    print("2. Remover item da lista")
    print("3. Exibir lista de compras")
    print("4. Sair")

    pergunta = int(input("Qual opção voce deseja: "))

    match pergunta:
        case 1:
            item = input("O que deseja adicionar na lista? ")

            listaItens.append(item)
        case 2:
            item = input("O que deseja remover? ")

            if item in listaItens:
                listaItens.remove(item)                 
        case 3:
            for i in listaItens:
                print(i, end=', ')
            
            print("Lista impressa!")
        case 4:
            print("Saindo ...")

            break
        case _:
            print("Opção inválida!")
    
    print("Cadastro finalizado!")