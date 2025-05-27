# List comprehension 
# Filtrar elementos	[x for x in lista if x > 0]
# Substituir ou transformar valores	[0 if x < 0 else x for x in lista]

# 1
listaNumeros = []

for i in range (1, 51):
    listaNumeros.append(i)
print(listaNumeros)

dobro = [numero * 2 for numero in listaNumeros]
print(dobro)

# 2
listaNomes = ['wrbr', 'swrr', 'wrbr', 'wrbr', 'wrbr', 'ernwr', 'wrbr', 'wrbr', 'r', 'wrbr', 'wrbr', 'wrbr', 'wrbr', 'wrbr', 'wrbr']

maiuscula = [nome.upper() for nome in listaNomes]
print(maiuscula)

# 3
listaPrecos = [3.56, 6.90, 3.21, 7.89, 3, 6, 90, 5.67, 3.4, 19.0]

listaDesconto = [preco * 0.9 for preco in listaPrecos]
print(listaDesconto)

# 4
listaNumerosMisturados = [1, 5, 6.7, 8.2, 6, 1, -7, -4, 0, 56]

listaAtualizada = [0 if num < 0 else num for num in listaNumerosMisturados]
print(listaAtualizada)

# 5
listaNomesEmail = ['heitor', 'baerbawfna', 'beafnsd', 'garaeh']

comEmail = [nome + '@gmail.com' for nome in listaNomesEmail]
print(comEmail)

# 6
listaNone = [12,58,46,None,69,47,None,None,None,100]

listaSemNone = ['Indefinido' if char == None else char for char in listaNone]
print(listaSemNone)

# 7
lista = []

for i in range(1, 50001):
    lista.append(i)

listaPares = [numero for numero in lista if numero % 2 == 0]

print("Existe {} numeros partes" .format(len(listaPares)))

# 8
listaValores = [1, 6, 4.5, 9, 9.3, 5, 8, 1, 9.0, 43]

listaQuadrado = [valor * valor for valor in listaValores]
print(listaQuadrado)

# 9
frase = 'Nos temos que acompanhar os jogos do flamengo'

fraseQuebrada = frase.split(' ')
palavrasLonga = [palavra for palavra in fraseQuebrada if len(palavra) > 5]
print(palavrasLonga)