contatos = {}

def menu ():
    print("1 - Adicionar Contato")
    print("2 - Alterar Contato")
    print("3 - Remover Contato")
    print("4 - Lista Contato")
    print("5 - Sair")
    
def adicionarContato ():
    p = input("Digite o nome do contato: ")
    n = int(input("Digite o telefone de contato: "))
    
    return p, n

def adicionarPessoas (p, n):
    contatos[p] = n
    
def alterarContato (antigo, novo, numeroNovo):
    if antigo in contatos:   
        contatos.pop(antigo)
        contatos[novo] = numeroNovo
    else:
        print("O contato nao existe!")
            
def removerContato (nome):
    contatos.pop(nome)

while True:
    menu()
    opcao = str(input("Escolha uma opção: "))
    
    match opcao:
        case '1':
            pessoa, numero = adicionarContato()
            
            adicionarPessoas(pessoa, numero)
            
            print("Contato adicionado com sucesso!")
        case '2':
            nomeAlterar = input("Qual o nome do contato que deseja alterar: ")
            novoNome = input("Qual vai ser o nome do novo contato: ")
            novoNumero = input("Qual vai ser o telefone do novo contato: ")
            
            alterarContato(nomeAlterar, novoNome, novoNumero)
            
            print("Contato alterado com sucesso!")
        case '3':
            nomeRemover = input("Qual o contato que voce deseja remover? ")
            
            removerContato(nomeRemover)
            
            print("Contato removido com sucesso!")
        case '4':
            for nome, telefone in contatos.items():
                print("{} - {}\n" .format(nome, telefone))
                
            if (len(contatos) == 0):
                print("Não a contatos cadastrado!")
            else:
                print("Contatos listados com sucesso!")
        case '5':
            print("Saindo...")
            break
        case _:
            print("Opção inválida!")