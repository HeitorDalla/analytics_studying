import pandas as pd

df = pd.read_csv('bibliotecas/pandas/teoria/relatorioAbril.csv')

print(df)

# Descrição geral do dados

print(df.dtypes)

print(df.columns)

print(df.values)

print(df.describe()) # Funciona somente em colunas numéricas


# Selecionar algumas linhas - Head, tail, loc, iloc

print(df.head(4))

print(df.tail(1))

serie = pd.Series(['Heitor', 'Gilmar', 'Marli', 'Nadir'], index=['nome1', 'nome2', 'nome3', 'nome4'])

print(serie)

# loc - seleciona pelo índice

print(serie.loc['nome1'])

print(serie.loc['nome4'])

# iloc - selecione pela posição

print(serie.iloc[2])

print(serie.iloc[-1])

# Selecionar alguma coluna

print(df['produto'])

print(df[df['quantidade'] > 10])


# Outras Funções

# Crosstab
dataframe = pd.read_csv('bibliotecas/pandas/teoria/vendas.csv')

tabelaComparativa = pd.crosstab(dataframe['data'], dataframe['produto'], margins=True) # Adiciona uma coluna e uma linha com a somatória geral

tabelaComparativa.to_csv('bibliotecas/pandas/teoria/tabelaComparativa.csv')

# Groupby
mediaPreco = dataframe.groupby(['produto']).mean()

print(mediaPreco)