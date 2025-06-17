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

# EXERCÍCIO 4 - INTERMEDIÁRIO
"""
Crie um sistema de inventário. Dada uma lista de transações,
implemente funções para:
- Encontrar itens com estoque baixo (< 10)
- Calcular valor total do inventário
"""

def exercicio4():
    transacoes = [
        {"item": "notebook", "tipo": "entrada", "quantidade": 50, "preco": 2500.00},
        {"item": "mouse", "tipo": "entrada", "quantidade": 100, "preco": 25.00},
        {"item": "notebook", "tipo": "saida", "quantidade": 15, "preco": 2500.00},
        {"item": "teclado", "tipo": "entrada", "quantidade": 5, "preco": 80.00},
        {"item": "mouse", "tipo": "saida", "quantidade": 95, "preco": 25.00}
    ]
    
    itensEstoqueBaixo = []
    totalInventario = 0

    for transacao in transacoes:
        if (transacao['quantidade'] < 10):
            itensEstoqueBaixo.append(transacao['item'])
        
        totalInventario += totalInventario + transacao['preco']
    
    return itensEstoqueBaixo, totalInventario

print(exercicio4())

# =============================================================================
# EXERCÍCIO 5 - INTERMEDIÁRIO/AVANÇADO
# =============================================================================
"""
Processamento de logs de acesso. Dada uma lista de strings de log,
extraia e analise:
- IPs únicos que acessaram o sistema
- Páginas mais acessadas (ordenadas por frequência)
- Horários de pico (por hora)
- IPs suspeitos (mais de 10 acessos)

Formato do log: "2024-01-15 10:30:25 192.168.1.100 GET /home 200"
"""

def exercicio5():
    logs = [
        "2024-01-15 10:30:25 192.168.1.100 GET /home 200",
        "2024-01-15 10:31:15 192.168.1.101 GET /login 200",
        "2024-01-15 11:15:30 192.168.1.100 POST /login 200",
        "2024-01-15 11:16:45 192.168.1.102 GET /home 200",
        "2024-01-15 14:20:10 192.168.1.100 GET /profile 200",
        "2024-01-15 14:21:30 192.168.1.100 GET /home 200",
        "2024-01-15 14:22:00 192.168.1.100 GET /settings 200",
        "2024-01-15 15:30:25 192.168.1.100 GET /home 200",
        "2024-01-15 15:31:15 192.168.1.100 GET /login 200",
        "2024-01-15 16:15:30 192.168.1.100 POST /login 200",
        "2024-01-15 16:16:45 192.168.1.100 GET /home 200",
        "2024-01-15 17:20:10 192.168.1.100 GET /profile 200",
        "2024-01-15 17:21:30 192.168.1.100 GET /home 200",
    ]
    
    # Sua solução aqui
    pass

# =============================================================================
# EXERCÍCIO 6 - AVANÇADO
# =============================================================================
"""
Sistema de recomendação simples. Dados usuários e seus filmes favoritos,
implemente:
- Encontrar usuários com gostos similares (baseado em filmes em comum)
- Recomendar filmes para um usuário baseado em similaridade
- Criar grupos de usuários por gênero preferido (gênero com mais filmes)
"""

def exercicio6():
    usuarios_filmes = {
        "Alice": {"Ação": ["Matrix", "John Wick"], "Drama": ["Titanic"]},
        "Bob": {"Ação": ["Matrix", "Vingadores"], "Comédia": ["Todo Mundo em Pânico"]},
        "Carol": {"Drama": ["Titanic", "A Culpa é das Estrelas"], "Romance": ["Notebook"]},
        "David": {"Ação": ["John Wick", "Vingadores"], "Ficção": ["Blade Runner"]},
        "Eva": {"Drama": ["Titanic"], "Romance": ["Notebook", "Orgulho e Preconceito"]}
    }
    
    # Sua solução aqui
    pass

# =============================================================================
# EXERCÍCIO 7 - AVANÇADO
# =============================================================================
"""
Análise de texto avançada. Dada uma lista de documentos (strings),
implemente:
- Índice invertido (palavra -> lista de documentos que a contêm)
- Contagem de frequência de palavras por documento
- Encontrar documentos mais similares (baseado em palavras em comum)
- Palavras mais importantes (que aparecem em poucos documentos)

Dica: Use regex para extrair palavras e normalize para minúsculas
"""

def exercicio7():
    documentos = [
        "Python é uma linguagem de programação versátil e poderosa",
        "Java é uma linguagem orientada a objetos muito popular",
        "Python e Java são linguagens de programação muito utilizadas",
        "Programação em Python é simples e intuitiva para iniciantes",
        "A linguagem Java oferece robustez para aplicações empresariais"
    ]
    
    # Sua solução aqui
    pass

# =============================================================================
# EXERCÍCIO 8 - AVANÇADO
# =============================================================================
"""
Sistema de cache inteligente. Implemente um cache LRU (Least Recently Used)
que:
- Armazena pares chave-valor com limite de tamanho
- Remove itens menos recentemente usados quando cheio
- Mantém estatísticas de hit/miss
- Tem métodos get() e put()

Teste com uma sequência de operações e mostre o estado do cache
"""

def exercicio8():
    class CacheLRU:
        def __init__(self, capacidade_maxima=3):
            # Inicializar estruturas de dados necessárias
            pass
        
        def get(self, chave):
            # Implementar busca no cache
            pass
        
        def put(self, chave, valor):
            # Implementar inserção no cache
            pass
        
        def get_stats(self):
            # Retornar estatísticas do cache
            pass
    
    # Teste o cache com estas operações:
    # cache.put("a", 1)
    # cache.put("b", 2)  
    # cache.put("c", 3)
    # cache.get("a")      # deve ser hit
    # cache.put("d", 4)   # deve remover "b"
    # cache.get("b")      # deve ser miss
    
    # Sua solução aqui
    pass

# =============================================================================
# EXERCÍCIO 9 - MUITO AVANÇADO
# =============================================================================
"""
Sistema de roteamento de grafos. Dado um grafo representado por dicionário,
implemente:
- Busca em largura (BFS) para encontrar caminho mais curto
- Encontrar todos os caminhos possíveis entre dois nós
- Detectar se existe ciclo no grafo
- Encontrar componentes conectados (grupos de nós conectados)
"""

def exercicio9():
    # Grafo representado como dicionário de adjacência
    grafo = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E', 'G'],
        'G': ['F'],
        'H': ['I'],  # Componente separado
        'I': ['H']
    }
    
    def bfs_caminho_minimo(inicio, fim):
        # Implementar BFS para caminho mais curto
        pass
    
    def todos_caminhos(inicio, fim):
        # Encontrar todos os caminhos possíveis
        pass
    
    def detectar_ciclos():
        # Detectar se há ciclos no grafo
        pass
    
    def componentes_conectados():
        # Encontrar componentes conectados
        pass
    
    # Sua solução aqui
    pass

# =============================================================================
# EXERCÍCIO 10 - EXPERT
# =============================================================================
"""
Sistema de processamento de dados em tempo real (simulado).
Implemente um pipeline que:
- Processa stream de eventos (lista de dicionários)
- Mantém janela deslizante de eventos recentes
- Calcula métricas em tempo real (contadores, médias)
- Detecta anomalias (valores muito acima da média)
- Gera alertas baseados em padrões
- Mantém histórico de métricas

Cada evento tem: timestamp, user_id, action, value
"""

def exercicio10():
    # Simulação de stream de dados
    eventos = [
        {"timestamp": 1, "user_id": "u1", "action": "login", "value": 1},
        {"timestamp": 2, "user_id": "u2", "action": "purchase", "value": 100},
        {"timestamp": 3, "user_id": "u1", "action": "view", "value": 1},
        {"timestamp": 4, "user_id": "u3", "action": "purchase", "value": 200},
        {"timestamp": 5, "user_id": "u2", "action": "purchase", "value": 50},
        {"timestamp": 6, "user_id": "u1", "action": "purchase", "value": 1000},  # Possível anomalia
        {"timestamp": 7, "user_id": "u4", "action": "login", "value": 1},
        {"timestamp": 8, "user_id": "u2", "action": "view", "value": 1},
        {"timestamp": 9, "user_id": "u3", "action": "purchase", "value": 150},
        {"timestamp": 10, "user_id": "u1", "action": "purchase", "value": 2000}, # Possível anomalia
    ]
    
    class ProcessadorTempoReal:
        def __init__(self, tamanho_janela=5):
            # Inicializar estruturas para janela deslizante,
            # métricas, alertas, etc.
            pass
        
        def processar_evento(self, evento):
            # Processar um evento: atualizar janela,
            # calcular métricas, detectar anomalias
            pass
        
        def detectar_anomalias(self, evento):
            # Detectar se o evento é anômalo
            pass
        
        def get_metricas_atuais(self):
            # Retornar métricas da janela atual
            pass
        
        def get_alertas(self):
            # Retornar todos os alertas gerados
            pass
    
    # Processar todos os eventos e retornar
    # métricas finais e alertas
    
    # Sua solução aqui
    pass

# =============================================================================
# INSTRUÇÕES PARA RESOLUÇÃO
# =============================================================================
"""
COMO USAR ESTE ARQUIVO:

1. Leia cada exercício cuidadosamente
2. Implemente sua solução na seção "# Sua solução aqui"
3. Teste suas funções executando-as individualmente
4. Compare seus resultados com o esperado

PROGRESSÃO DE DIFICULDADE:
- Exercícios 1-2: Manipulação básica de strings e estruturas
- Exercícios 3-4: Combinação de estruturas e lógica de negócio
- Exercícios 5-6: Algoritmos intermediários e análise de dados
- Exercícios 7-8: Estruturas de dados avançadas
- Exercícios 9-10: Algoritmos complexos e sistemas completos

DICAS GERAIS:
- Use conjuntos (sets) para eliminar duplicatas
- Use dicionários para contagens e agrupamentos
- Use listas para manter ordem
- Use compreensões de lista/dicionário quando apropriado
- Pense na eficiência dos algoritmos para exercícios avançados

BOA SORTE!
"""