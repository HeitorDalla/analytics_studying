# 10 EXERCÍCIOS DE MANIPULAÇÃO DE DADOS - BÁSICO AO AVANÇADO

# EXERCÍCIO 1 - BÁSICO
"""
Crie uma função que receba uma lista de nomes e retorne:
- Um dicionário com a primeira letra como chave e lista de nomes como valor
- A quantidade total de caracteres de todos os nomes

Exemplo de entrada: ["Ana", "Bruno", "Carlos", "Alice", "Beatriz", "Antonio"]
Exemplo de saída: ({'A': ['Ana', 'Alice', 'Antonio'], 'B': ['Bruno', 'Beatriz'], 'C': ['Carlos']}, 32)
"""

def exercicio1():
    nomes = ["Ana", "Bruno", "Carlos", "Alice", "Beatriz", "Antonio"]
    nomes.sort()
    totalCaracter = 0

    nomeTamanho = {}  

    for nome in nomes:
        letra = nome[0]
        totalCaracter += len(nome)

        if letra not in nomeTamanho:
            nomeTamanho[letra] = []

        nomeTamanho[letra].append(nome)

    return (nomeTamanho, totalCaracter)

print(exercicio1())

# EXERCÍCIO 2 - BÁSICO/INTERMEDIÁRIO
"""
Dada uma string, crie uma função que retorne:
- Um conjunto com todas as palavras únicas (sem repetição)
- Um dicionário com cada palavra e sua frequência
- A palavra mais longa

Exemplo: "python é incrível python facilita programação programação é arte"
"""

def exercicio2():
    texto = "python é incrível python facilita programação programação é arte"
    
    string = texto.split(" ")
    palavrasUnicas = set()
    palavraSequencia = {}
    maiorTamanho = -99999
    maiorPalavra = ''

    for palavra in string:
        if (palavra not in palavrasUnicas):
            palavrasUnicas.add(palavra)

            palavraSequencia[palavra] = 1
        else:
            palavraSequencia[palavra] += 1

        if len(palavra) > maiorTamanho:
            maiorTamanho = len(palavra)
            maiorPalavra = palavra
    
    return palavrasUnicas, palavraSequencia, maiorPalavra

print(exercicio2())

