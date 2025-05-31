import pandas as pd
from datetime import date, time, datetime, timedelta

df = pd.read_csv('bibliotecas/pandas/pratica3/IMDB Top 250 Movies.csv', sep=',', encoding='utf-8', parse_dates=['year'])

# Diretores mais recorrentes
diretoresRecorrentes = df['directors'].value_counts()
print(diretoresRecorrentes.head(5))
print("---------------------------")

# Média das avaliações
mediaAvaliacoes = df['rating'].mean()
print("A média das avaliações é: {}" .format(mediaAvaliacoes))
print("---------------------------")

# Quais os filmes mais antigos e recentes
maisAntigos = df.value_counts()
print("Os filmes mais antigos é: ")
print(maisAntigos.tail(5))

maisNovos = df.value_counts()
print("Os filmes mais novos é: ")
print(maisNovos.head(5))

# Filmes separados por dácada
# Transformar a colune de year em objeto data
df['year'] = pd.to_datetime(df['year'])
# Criar uma coluna para extrair o ano
df['ano'] = df['year'].dt.year
# Criar uma coluna para calcular as décadas
df['decada'] = (df['ano'] // 10) * 10
# Contagem dos filmes por década
contagemFilmes = df['decada'].value_counts().sort_index()
print(contagemFilmes)

# Pesquisar qual o gênero é mais frequência
agrupamentoGenero = df['genre']

print("O gênero mais frequente é: {}" .format(agrupamentoGenero.max()))
print("O gênero menos frequente é: {}" .format(agrupamentoGenero.min()))

# Ver quais são os 10 melhores e 10 piores filmes de acordo com as avaliações
melhoresFilmes = df.sort_values(by='rating', ascending=False).head(10)
print("As dez melhores avaliações são: {}" .format(melhoresFilmes[['name', 'rating']]))

pioresFilmes = df.sort_values(by='rating', ascending=False).tail(10)
print("As dez piores avaliações são: {}" .format(pioresFilmes[['name', 'rating']]))