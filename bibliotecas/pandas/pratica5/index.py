import pandas as pd

df = pd.read_csv('bibliotecas/pandas/pratica5/IMDB Top 250 Movies.csv', sep=',', encoding='utf-8', parse_dates=['year'])

def converter_para_minutos(duracao):
    partes = duracao.strip().split(' ')
    minutos = 0
    for parte in partes:
        if 'h' in parte:
            minutos += int(parte.replace('h', '')) * 60
        elif 'm' in parte:
            minutos += int(parte.replace('m', ''))
    return minutos

# Coluna dentro da tabela que converte a quantidade de horas para minutos
df['duracao_min'] = df['run_time'].apply(converter_para_minutos)
print(df['duracao_min'])

# Categorizando cada duracao com seu respectivo tempo de duração
df['Categoria_Duracao'] = df['duracao_min'].apply(lambda duracao: 'CURTO' if duracao < 90 else 'MÉDIO' if duracao >= 90 and duracao <= 150 else 'LONGO')
print(df['Categoria_Duracao'])

# Mostre quantos filmes tem por categoria
quantidadePorCategoria = df.groupby('Categoria_Duracao')['rank'].count()
print("A quantidade de filmes por categoria é: {}" .format(quantidadePorCategoria))

# Mostrar a nota média de cada categoria
mediaPorCategoria = df.groupby('Categoria_Duracao')['rating'].mean()
print("A nota média por categoria é: {}" .format(mediaPorCategoria))

# Mostrar a categoria mais comum no top 250
maisComum = df.groupby('Categoria_Duracao')['rank'].count()
print("A categoria com mais filmes é: {} com {} filmes" .format(maisComum.idxmax(), maisComum.max()))

# Fazer um relatório com todas as informações
relatorioFilmes = pd.DataFrame({
    'nomeCategoria': quantidadePorCategoria.index,
    'quantidadeFilmes': df.groupby('Categoria_Duracao')['rank'].count().sort_values(ascending=False),
    'notaMediaCategoria': df.groupby('Categoria_Duracao')['rating'].mean()
})

relatorioFilmes.to_csv('bibliotecas/pandas/pratica5/relatorioFilmes.csv')


# Filmes por duração

# Filmes lançados por ano
df['anoLançamento'] = df['year'].dt.year

filmesAno = df.groupby('anoLançamento')['rank'].count()
print(filmesAno.sort_values(ascending=False))

# Ano que teva mais filme no top 250
anoTop = df.groupby('anoLançamento')['rank'].count().idxmax()
print("O ano que teve mais filme dentro do top 250 foi: {}" .format(anoTop))

# Filmes lançados entre 1990 e 1999 com nota acima de 3
entreAnos = df.loc[(df['year'].dt.year >= 1990) & (df['year'].dt.year <= 1999)]
# Filtrando apenas aqueles com nota maior que 3
notaAcima = entreAnos.loc[entreAnos['rating'] > 3]
print("Os filmes lançados entre 1990 e qua tiveram uma nota maior que 3: {}" .format(notaAcima))

entreAnos.to_csv('bibliotecas/pandas/pratica5/relatorioFilmeAno.csv')


# Relatório textual

# Filme com 'Love' no titulo
nomesLove = df.loc[df['name'].str.contains('Love', case=False)]
print("Dentro todos os filmes, os que contem a palavra love é: {}" .format(nomesLove))

# Listar os filmes que contem 'War' 'God' ou 'King'
nomesFiltrados = df.loc[df['name'].str.contains('War|God|King', case=False)]
print("Os filmes que contem em seus titulos as palavras war, god e king é: {}" .format(nomesFiltrados))

# Criar uma nova coluna com os titulos em letras maiusculas
df['titulo_maiusculo'] = df['name'].str.upper()
print("Todos os títulos em letras maiúsculas: {}" .format(df['titulo_maiusculo']))

# Títulos que tem mais de 25 caracteres
titulosCaracteres = df.loc[df['name'].astype(str).str.len() > 25]
print(titulosCaracteres)

# Qual o título mais longo da lista
titulosLongo = df['name'].astype(str).str.len().idxmax()

nomeMaisLongo = df.loc[titulosLongo, ['name']]
print("O filme com título com longo da lista é: {}" .format(nomeMaisLongo))


# Filtros múltiplos

# 6.1. Mostrar todos os filmes com nota >= 9
duracaoFiltrada = df['run_time'].apply(converter_para_minutos).astype(float)
notaMaior9 = df.loc[(df['rating'] >= 8) & (df['year'].dt.year > 2000) & (duracaoFiltrada <= 100)]
print(notaMaior9)

# 6.2. Filtre os filmes que:
# Têm duração entre 120 e 150 minutos
# Foram dirigidos por “Christopher Nolan”
# Estão entre os 50 primeiros do ranking
# Exporte o resultado de 9.2 para filmes_nolan.csv
diretorChristopher = df.loc[
    ((df['duracao_min'] >= 120) & (df['duracao_min'] <= 150)) & 
    (df['directors'].str.contains('Christopher Nolan', case=False, na=False))
].sort_values(by='rank')
resultado = diretorChristopher.head(50)

resultado.to_csv('bibliotecas/pandas/pratica5/filmes_nolan.csv')

# 6.3. Mostre os filmes com título iniciado pela letra “A” e nota acima de 8.0.
iniciadosA = df[
    (df['name'].str.startswith('A', na=False)) & 
    (df['rating'] > 8)
]
print("Os filmes com letras inciadas com A são: {}" .format(iniciadosA))

iniciadosA.to_csv('bibliotecas/pandas/pratica5/filmasA.csv')

# 6.4. Liste todos os filmes que não foram dirigidos por “Steven Spielberg”.
notSpilberg = df[~df['directors'].str.contains('Steven Spielberg', case=False, na=False)]
print(notSpilberg)

notSpilberg.to_csv('bibliotecas/pandas/pratica5/notSpilberg.csv')