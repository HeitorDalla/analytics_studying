# Entendendo a funcão anônimoa Lambda

# Dobrar um número
numero1 = int(input("Digite um numero para dobrar: "))
dobrarNumero = lambda n: n * 2

print("O numero {} dobrado é: {}" .format(numero1, dobrarNumero(numero1)))

# Calcular a soma de dois numeros
numeroOne = int(input("Digite um numero: "))
numeroTwo = int(input("Digite outro numero: "))

somarNumeros = lambda x, y: x + y
print("A soma dos numeros {} e {} é: {}" .format(numeroOne, numeroTwo, somarNumeros(numeroOne, numeroTwo)))

# Verificar se o numero é par
numeroVerificar = int(input("Digite um numero para a verificacao se ele é par: "))

verificar = lambda numero: 'NÃO É PAR' if numero % 2 != 0 else 'É PAR'
print("O numero {} {}" .format(numeroVerificar, verificar(numeroVerificar)))


# Sorted

# Ordenando uma lista de pessoas com o Sorted e Lambda
dicionarioPessoa = [
    (
        'Heitor', 18
    ),
    (
        'Gilmar', 52 
    )
]

pessoasOrdenadas = sorted(dicionarioPessoa, key = lambda pessoa: pessoa[1], reverse=True)

print(pessoasOrdenadas)


# Filter

# Usando o Filter com o Lambda para obter apenas os números pares
listaNumeros = [1, 56, 23, 89, 342, 4, 45, 8 , 6, 3]

listaFiltrada = list(filter(lambda numero: numero % 2 == 0, listaNumeros))

print(listaFiltrada)

# Usando o Filter para pegar os nomes de uma lista, para pegar apenas as palavras que começam com a letra A
elementosArray = ['aranha', 'banana', 'agua', 'butina', 'cachorro',
'anel','aliança','cabrito','zebra','cola','azul','amarelo','roxo','rosa']

elementoFiltrados = list(filter(lambda elemento: elemento[0] == 'a', elementosArray))
print(elementoFiltrados)

# Filtrando uma lista de nomes e pegar aquelas que sao extamente 'Alice'
nomes = ['alice', 'roberto', 'thiago', 'alice']

nomesFiltrados = list(filter(lambda nome: nome == 'alice', nomes))
print(nomesFiltrados)
print("Os nomes achados foram: ")

for nome in nomesFiltrados:
    print(nome)
    
    
# Map

# Utilizando o Map, vamos retornar de uma lista todos os numeros dobrados
listaNumbers = [1, 2, 3, 4, 5]

numerosDobrados = list(map(lambda numero: numero ** 2, listaNumbers))
print(numerosDobrados)

# Transformar uma lista de palavras em uma lista que contem o comprimento de cada palavra
nomesLista = ['aranha', 'banana', 'agua', 'butina', 'cachorro',
'anel','aliança','cabrito','zebra','cola','azul','amarelo','roxo','rosa']

tamanhoPalavras = list(map(lambda nome: len(nome), nomesLista))
print(tamanhoPalavras)