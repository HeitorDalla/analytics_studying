import pandas as pd

# Leitura do arquivo
df = pd.read_csv('bibliotecas/pandas/pratica2/feedbacks.csv', sep=',', encoding='utf-8')

# Cálculo da média por curso
mediaNotas = df.groupby('curso')['nota'].mean().round(2)

print(mediaNotas)

# Identificar o curso com melhor e pior avaliação
agrupamento = df.groupby('curso')['nota'].sum()
cursoMelhorAvaliacao = agrupamento.idxmax()
notaMaior = agrupamento.min()

print("A pior avaliação é do curso {} com {} de avaliação" .format(cursoMelhorAvaliacao, notaMaior))

cursoMenorAvaliacao = agrupamento.idxmin()
notaMenor = agrupamento.max()
print("A pior avaliação é do curso {} com {} de avaliação" .format(cursoMenorAvaliacao, notaMenor))

# Quantas pessoas recomendaram por curso
agrupamentoCurso = df.groupby('curso')['recomendaria'].count()

recomendaria = df[df['recomendaria'] == 'Sim']
recomendaria2 = recomendaria.groupby('curso')['recomendaria'].count()
print(recomendaria2)

# Ver quantidade de feedbacks por dia
agrupamentoDia = df.groupby('data').size()
print(agrupamentoDia)

# Filtrar só os feedbacks negativos (nota <= 2)
relatorioFeedbacksNegativos = df.loc[df.nota <= 2]

relatorioFeedbacksNegativos.to_csv('bibliotecas/pandas/pratica2/relatorioNegativos.csv', index=False)
print(relatorioFeedbacksNegativos)