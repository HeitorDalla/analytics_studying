def menu ():
    print("1 - Ver disposição dos assentos")
    print("2 - Deservar um assento")
    print("3 - Sair")

def carregarMatriz ():
    matriz = []
    for linha in range(5):
        linhaMatriz = []
        for coluna in range(10):
            linhaMatriz.append('D')
        matriz.append(linhaMatriz)
    return matriz

def reservarAssento (linha, coluna):
    if (matriz[linha][coluna] == 'D'):
        matriz[linha][coluna] = 'R'
    else:
        print("O lugar ja esta ocupado!") 

matriz = carregarMatriz()

while True:
    menu()

    pergunta = input("Escolha uma opção: ")

    match pergunta:
        case '1':
            print(matriz, end=' ')
        case '2':
            linha = int(input("Digite o numero da fileira (linha 0-4): "))
            coluna = int(input("Digite o numero da assento (linha 0-9): "))
            reservarAssento(linha, coluna)
        case '3':
            print("Saindo...")
            break
        case _:
            print("Esse opção não esta disponível!")
