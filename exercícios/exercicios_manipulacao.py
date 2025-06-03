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

# EXERCÍCIO 3 - INTERMEDIÁRIO
"""
Você tem uma lista de dicionários representando estudantes.
Crie uma função que retorne:
- Conjunto de todas as disciplinas cursadas
- Dicionário com média de notas por disciplina
- Lista dos 3 melhores estudantes (por média geral)
"""

def exercicio3():
    estudantes = [
        {"nome": "João", "notas": {"Matemática": 8.5, "Português": 7.0, "História": 9.0}},
        {"nome": "Maria", "notas": {"Matemática": 9.0, "Português": 8.5, "Física": 8.0}},
        {"nome": "Pedro", "notas": {"História": 7.5, "Física": 9.5, "Português": 8.0}},
        {"nome": "Ana", "notas": {"Matemática": 9.5, "História": 8.5, "Física": 9.0}}
    ]

    disciplinas = set()
    somaNotas = {}
    contNotas = {}
    
    for estudante in estudantes:        
        for materia, nota in estudante['notas'].items():
            disciplinas.add(materia)

            if materia not in somaNotas:
                somaNotas[materia] = 0
                contNotas[materia] = 0
            
            somaNotas[materia] += nota
            contNotas[materia] += 1

    mediaNotaDisciplina = {}

    for materia in disciplinas:
        mediaNotaDisciplina[materia] = somaNotas[materia] / contNotas[materia]

    # média de todos os estudantes
    mediaEstudantes = []
    for estudante in estudantes:
        notas = estudante['notas'].values()
        media = sum(notas) / len(notas)

        mediaEstudantes.append((estudante['nome'], media))

    # os três com melhores notas
    melhores = sorted(mediaEstudantes, key=lambda x: x[1], reverse=True)[:3]
                
    return disciplinas, mediaNotaDisciplina, melhores

print(exercicio3())

