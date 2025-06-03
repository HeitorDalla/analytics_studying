# Forma mais breve de criar um dicionário

# Lista
numeroQuadradosLista = [x ** 2 for x in range(1, 11)]
print(numeroQuadradosLista)

# Dicionário
numeroQuadradoDicionario = {x: x ** 2 for x in range(1, 11)}
print(numeroQuadradoDicionario)

# Exercicio - Transformar um conjunto em dicionario com palavras e seus comprimentos
palavras = {'Python', 'JavaScript', 'Java', 'TypeScript'}
palavraComprimento = {}

for palavra in palavras:
    palavraComprimento[palavra] = len(palavra)

print(palavraComprimento)

# usando o Dictionary Comprehension
palavras2 = {'Python', 'JavaScript', 'Java', 'TypeScript'}
comprimentos = {palavra: len(palavra) for palavra in palavras2}

print(comprimentos)

# Exercicio - Tranformando os valores em chaves e os valores sao o quadrado desses numeros
numeros = [1, 2, 3, 4, 5]
quadrado = {numero: numero*numero for numero in numeros}

print("Os quadrados dos numero é: {}" .format(quadrado))

# Exercicio com dicionários e funções

# 1
def registrar_livro (titulo, autor, ano):
    return {
        'titulo': titulo,
        'autor': autor,
        'ano': ano
    }

novoLivro = registrar_livro("Deixa acontecer naturalmente", 'Desconhecido', 2000)

print("O novo livro é: ")
for chave, valor in novoLivro.items():
    print("{}: {}" .format(chave, valor))

# 2
def exibirLivro (dicionario):
    for chave, valor in dicionario:
        print("{}: {}" .format(chave, valor))

livroObjeto = {
    'titulo': 'Noites escuras',
    'autor': 'desconhecido',
    'ano': 1980
}

print("O livro em detalhes: {}" .format(livroObjeto))