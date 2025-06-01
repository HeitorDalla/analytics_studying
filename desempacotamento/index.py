# Técnica que permite extrair valores individuais de uma estrutura de dados e atribuir à variáveis separadas.

# 1
pacote_viagem = ("Paris", 5, 1500)

destino, noites, preco = pacote_viagem

print("O destino é: {}" .format(destino))
print("O numero de noites é: {}" .format(noites))
print("O preco da viagem é: {}" .format(preco))

# 2
pessoa = ("João", 25, "Engenheiro")

nome, idade, trabalho = pessoa

print("{} tem {} anos e trabalha como {}" .format(nome, idade, trabalho))

# 3
coordenadas = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]

primeiro, _, _, _, ultimo = coordenadas
print("Os primeiras coordenadas é: {} \nE as últimas coordenadas é: {}" .format(primeiro, ultimo))

# 4
def vendas_anuais():
    return [15000, 18000, 22000, 25000, 19000, 21000, 24000, 26000, 20000, 23000, 27000, 30000]

q1, q2, q3, *demais = vendas_anuais()

soma = 0
cont = 0

for i in demais:
    soma += i
    cont += 1

media = soma / cont

print("A média dos 3 primeiros valores é: {}\n E a média dos demais valores é: {}" .format(((q1 + q2 + q3) / 3), media))

# 5
def processar_dados(*args, **kwargs):
    soma = 0
    qtd = 0
    # A função deve:
    # 1. Somar todos os números em args
    # 2. Contar quantas chaves existem em kwargs
    # 3. Retornar uma tupla (soma, quantidade_chaves)
    for arg in args:
        soma += arg
    for dic in kwargs.keys():
        qtd += 1
        
    return [soma, qtd]
        
soma, qtd = processar_dados(1, 2, 3, nome="João", idade=30, cidade="SP")

print("A soma é: {} e a quantidade é: {}" .format(soma, qtd))