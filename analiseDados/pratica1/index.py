import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

df = pd.read_csv("analiseDados/pratica1/Life_Expectancy_Data.csv", sep=',', encoding='utf-8')

# 1. Os vários fatores de previsão inicialmente escolhidos realmente afetam a expectativa devida? 
# Quais são as variáveis de previsão que realmente afetam a expectativa de vida?
# 2. Um país com menor expectativa de vida (<65) deve aumentar seus gastos com saúde para melhorar sua expectativa de vida média?
# 3. Como as taxas de mortalidade infantil e adulta afetam a expectativa de vida?
# 4. A expectativa de vida tem correlação positiva ou negativa com hábitos alimentares, estilo de vida, exercícios, fumo, consumo de álcool etc.
# 5. Qual é o impacto da escolaridade na expectativa de vida dos seres humanos?
# 6. A expectativa de vida tem relação positiva ou negativa com o consumo de álcool?
# 7. Países densamente povoados tendem a ter menor expectativa de vida?
# 8. Qual é o impacto da cobertura de imunização na expectativa de vida?

# Pegando apenas os países em desenvolvimento
df = df[df['Status'] == 'Developing']

# Pergunta 1


# Pergunta 2

# Média da expectativa de vida dos países que tem a média de expectativa de vida menor que 65
# Expectativa de vida ao longo dos anos
# sns.lineplot(x='Year', y='Life expectancy', data=df, legend=False)
# plt.title("Espectativa de vida por país ao longo dos anos")
# plt.xlabel("Ano")
# plt.ylabel("Espectativa de vida")
# plt.show()

porPais = df.groupby('Country')['Life expectancy'].mean().sort_values()
menor65 = porPais[porPais < 65]

menor65Linhas = df[df['Country'].isin(menor65.index)].copy()

menor65Linhas['percentage expenditure'] = (
    menor65Linhas['percentage expenditure']
    .str.replace('.', '')
    .str.replace(',', '.')
    .astype(float)
)

mediaExpectativaMenorPaises65 = menor65Linhas['percentage expenditure'].mean()
print('{:.2f}' .format(mediaExpectativaMenorPaises65))

# Média da expectativa de vida dos países que tem a média de expectativa de vida maior que 65

maior65 = porPais[porPais > 65]

maior65Linhas = df[df['Country'].isin(maior65.index)].copy()

maior65Linhas['percentage expenditure'] = (
    maior65Linhas['percentage expenditure']
    .str.replace('.', '', regex=False)
    .astype(float)
)

mediaExpectativaMaiorPaises65 = maior65Linhas['percentage expenditure'].mean()
print('{:.2f}' .format(mediaExpectativaMaiorPaises65))

# Conclusão da pergunta 2:
# Os dados mostram que os países com expectativa de vida maior que 65 anos tendem a apresentar uma média maior de gasto com saúde (% do PIB),
# sugerindo que o investimento em saúde pública pode estar associado a uma maior expectativa de vida.