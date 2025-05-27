# 1
listaNumeros = []

for numero in range(1, 51):
    listaNumeros.append(numero)

for n in range(len(listaNumeros)):
    print("O dobro de {} é {}" .format(n, n * 2))

# 2
listaNomes = ['wrbr', 'swrr', 'wrbr', 'wrbr', 'wrbr', 'ernwr', 'wrbr', 'wrbr', 'r', 'wrbr', 'wrbr', 'wrbr', 'wrbr', 'wrbr', 'wrbr']

for i in listaNomes:
    print("O nome em maiusculo é: {}" .format(i.upper()))
    
# 3
listaPrecos = [3.56, 6.90, 3.21, 7.89, 3, 6, 90, 5.67, 3.4, 19.0]

for item in listaPrecos:
    print("O valor {} com desconto de 10% fica: {}" .format(item, item * 0.9))
    
# 4
listaNumerosMisturados = [1, 5, 6.7, 8.2, 6, 1, -7, -4, 0, 56]

for i in range(len(listaNumerosMisturados)):
    if (listaNumerosMisturados[i] < 0):
        listaNumerosMisturados[i] = 0
print(listaNumerosMisturados)

# 5
listaNomesEmail = ['webqwrbwrb', 'baerbawfna', 'beafnsd', 'garaeh']
listaNovaEmail = []

for nome in listaNomesEmail:
    listaNovaEmail.append(nome + '@gmail.com')

print(listaNovaEmail)

# 6
listaNone = [12,58,46,None,69,47,None,None,None,100]

for i in range(len(listaNone)):
    if (listaNone[i] == None):
        listaNone[i] = 'Indefinido'
        
print(listaNone)

# 7
contador = 0
for i in range (50000):
    if (i % 2 == 0):
        contador += 1
        
print(contador)

# 8
listaValores = [1, 6, 4.5, 9, 9.3, 5, 8, 1, 9.0, 43]
listaQuadrado = []

for i in listaValores:
    listaQuadrado.append(i * i)
    
print(listaQuadrado)

# 9
frase = 'Nos temos que acompanhar os jogos do flamengo'

fraseQuebrada = frase.split(' ')
for i in range(len(fraseQuebrada)):
    if (len(fraseQuebrada[i]) > 5):
        fraseQuebrada[i] = 'LONGA'

print(fraseQuebrada)

# 10
elementosArray = ['aranha', 'banana', 'agua', 'butina', 'cachorro',
'anel','aliança','cabrito','zebra','cola','azul','amarelo','roxo','rosa']

for i in range(len(elementosArray)):
    if (elementosArray[i][0] == 'a'):
        elementosArray[i] = '***'
        
print(elementosArray)

# 11
listaFrutas = ['banana', 'maçã', 'banana', 'laranja']

for i in range(len(listaFrutas)):
    if (listaFrutas[i] == 'banana'):
        listaFrutas[i] = 'abacaxi'

print(listaFrutas)

# 12
soma = 0
for i in range (50000):
    soma += i
print(soma)

# 13
listaNumbers = [1, 56, 23, 89, 342, 4, 45, 8 , 6, 3]
listaNumbersModificada = []

for i in range (len(listaNumbers)):
    if (listaNumbers[i] > 50):
        listaNumbersModificada.append(listaNumbers[i])
    
print(listaNumbersModificada)

# 15
notasAlunos = [[67, 34, 89, 60], [21, 67, 90, 100], [10, 62, 91, 70]]

for i in range (len(notasAlunos)):
    soma = 0
    for nota in range(len(notasAlunos[i])):
        soma += notasAlunos[i][nota]
    media = float(soma / 4)
    print("A soma das notas do aluno é: {}" .format(media))
    
    if (media >= 60):
        print("Voce esta aprovado!")
        print('\n--------------')
    else:
        print("Voce esta reprovado!")
        print('\n--------------')