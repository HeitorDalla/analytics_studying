def validacao (n):
    if n.isdigit():
        entrada = int(n)

        print("É um digito valido!")

        if entrada >= 0 and entrada <= 10:
            print("O numero esta dentro do intervalo!")
            return True
        else:
            print("O numero nao esta dentro o intervalo valido!")
            return False
    else:
        print("Não é um numero valido!")
        return False

nota = input("Digite uma nota de 1 a 10: ")

resultado = validacao(nota)

if resultado:
    print("A nota foi inserida com sucesso!")
else:
    print("A nota não foi inserida com sucesso!")