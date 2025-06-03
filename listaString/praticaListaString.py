# 1
itens = [1, 'teste', True, False, 'Heitor', 167, 'Exemplo', 67, False, True]
print(itens)

# 2
print(len(itens))
itens.append('TCS')
print(len(itens))

# 3
novosItens = [100, 200, 300]
itens.extend(novosItens)
print(itens)

# 4
itens.insert(2, 'meio')
print(itens)

# 5
itens.remove(100) # Caso o valor não existir, ele retornara um erro que o valor não existe
print(itens)

# 6
itemRemovido = itens.pop(3)
print(itemRemovido)
print(itens)

# 7
itens.clear()
print(itens)

# 8
listaFrutras = ['banana', 'pera', 'maca', 'kiwi']
indiceBanana = listaFrutras.index("banana")
print(indiceBanana)

# 9
contagem = listaFrutras.count('banana')
print(contagem)

# 10
listaFrutras.reverse()
print(listaFrutras)

# 11
stringTeste = 'python,java,c++'

lista = stringTeste.split(',')
print(lista)

# 12
listaJoin = ["py", "js", "rb"]
listaAlterada = " | ".join(listaJoin)
print(listaJoin)

# 13
stringHello = '   hello world   '
print(stringHello.strip())

# 14
stringTesteJuncao = '  aplle; banana; cherry   '
stringSemEspacos = stringTesteJuncao.strip()
stringSemEspacos.split(';')
print(stringSemEspacos)

# 15
nums = [1, 2, 3, 4]

while len(nums) > 0:
    numeroRemovido = nums.pop()
    print("Valor removido: {}" .format(numeroRemovido))
print(nums)

# 16
pergunta = input("Qual é o seu nome?")
modificada = pergunta.split(' ')
modificada.reverse()

stringConvertida = ' '.join(modificada)
print(stringConvertida)

# 17 - Mini Projeto
frutas = []

with open("estudandoPython/listaString/arquivoTeste.txt", "rt") as Arquivo:
    for linha in Arquivo.readlines():
        fruta = linha.strip()
        if (fruta):
            frutas.append(fruta)
    
print(frutas)
for fruta in frutas[:]:
    ocorrencia = frutas.count(fruta)
    if (ocorrencia > 1):
        frutas.remove(fruta)

frutas.sort()
print(frutas)