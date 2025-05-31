import pandas as pd
from datetime import date, time, datetime, timedelta

df = pd.read_csv('bibliotecas/pandas/pratica4/IMDB Top 250 Movies.csv', sep=',', encoding='utf-8', parse_dates=['year'])

# Análise de Décadas

# Transformar a coluna year em objeto data
df['year'] = pd.to_datetime(df['year'])
# Pegar apenas o ano
df['ano'] = df['year'].dt.year
# Filtrar por ano
df['decada'] = (df['ano'] // 10) * 10
# Fazer a contagem por decada
contagemDecada = df['decada'].value_counts()
print(contagemDecada)

# Década com mais filme
print("A década com mais filme é: {} com {} filmes." .format(contagemDecada.idxmax(),contagemDecada.max()))

# Para cada década calcule a nota média e duração média dos filmes
agrupandoDecadas = df.groupby('decada')['rating'].mean()
print("A média das notas notas por década é: ")
print(agrupandoDecadas)

# Duração média dos filmes
def to_minutes(s):
    try:
        h, m = s.split('h')
        return int(h.strip()) * 60 + int(m.replace('m', '').strip())

    except:
        return None

df['run_time'] = df['run_time'].apply(to_minutes).astype(float)
media_duracao = df['run_time'].mean()

print(f'Média de duração: {media_duracao:.2f} minutos')

# Salvar um resumo desse em um arquivo chamado resumo_decadas.csv
resumo_decadas = pd.DataFrame({
    'quantidade_filmes': df['decada'].value_counts().sort_index(),
    'nota_media': df.groupby('decada')['rating'].mean(),
    'duracao_media': df.groupby('decada')['run_time'].mean()
})

resumo_decadas.to_csv('resumo_decadas.csv')


# Diretores e frequência

# Juntar todos os diretores em uma lista separada
contagemDiretores = df['directors'].str.split(',').explode().str.strip()
print(contagemDiretores)
# Pegar apenas os únicos diretores da lista
diretoresUnicos = contagemDiretores.unique()
print(diretoresUnicos)
# Pegar a quantidade total de diferentes diretores
quantidade = len(diretoresUnicos)
print(quantidade)

# Diretores mais frequentes
diretoresFrequentes = df['directors'].value_counts()
print("O 5 diretores mais frequentes são: {}" .format(diretoresFrequentes.head(5)))

# Nota média dos filmes de cada diretor (exibir só quem tem mais de 3 filmes)
df['directors'] = df['directors'].str.split(',')
df = df.explode('directors')
df['directors'] = df['directors'].str.strip()

contagemFilmesDiretor = df['directors'].value_counts()

diretorMais3 = contagemFilmesDiretor[contagemFilmesDiretor >= 3].index
mediaFilmesDiretor = df.groupby('directors')['rating'].mean()
mediaFilmesDiretorMais3 = mediaFilmesDiretor.loc[diretorMais3]

print("A média dos diretores que possuem mais de 3 filmes é: {}" .format(mediaFilmesDiretorMais3.sort_values(ascending=False)))

# Qual diretor tem o filme mais bem avaliado
filmesMelhorAvaliado = df['rating'].max()
linhaMelhorAvaliado = df[df['rating'] == filmesMelhorAvaliado]
print("O diretor com o melhor filme avaliado é: {}" .format(linhaMelhorAvaliado['directors']))

# Exportar para csv o ranking com diretor, quantidade de filmes e nota média
# Nota média dos filmes de cada diretor (exibir só quem tem mais de 3 filmes)
df['directors'] = df['directors'].str.split(',')
df = df.explode('directors')
df['directors'] = df['directors'].str.strip()

ranking = df.groupby('directors').agg({
    'name': 'count',
    'rating': 'mean'
})

ranking.to_csv('bibliotecas/pandas/pratica4/ranking_diretores.csv')

print(df['decada'])