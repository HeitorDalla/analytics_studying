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

# Cabeçalho
df = df[df['Status'] == 'Developing']
st.header("Estatísticas sobre a expectativa de vida dos Países")


st.subheader('1. Os vários fatores de previsão inicialmente escolhidos realmente afetam a expectativa devida?') 


st.subheader('2. Um país com menor expectativa de vida (<65) deve aumentar seus gastos com saúde para melhorar sua expectativa de vida média?')

# Média da expectativa de vida dos países que tem a média de expectativa de vida menor que 65
# Expectativa de vida ao longo dos anos
fig, ax = plt.subplots()
sns.lineplot(x='Year', y='Life expectancy', data=df, legend=False, ax=ax)
plt.title("Espectativa de vida por país ao longo dos anos")
plt.xlabel("Ano")
plt.ylabel("Espectativa de vida")
st.pyplot(fig)

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
st.write("A média da expectativa de vida dos países que possuem a média de gastos menor que 65 é: {:.2f}" .format(mediaExpectativaMenorPaises65))

# Média da expectativa de vida dos países que tem a média de expectativa de vida maior que 65

maior65 = porPais[porPais > 65]

maior65Linhas = df[df['Country'].isin(maior65.index)].copy()

maior65Linhas['percentage expenditure'] = (
    maior65Linhas['percentage expenditure']
    .str.replace('.', '', regex=False)
    .astype(float)
)

mediaExpectativaMaiorPaises65 = maior65Linhas['percentage expenditure'].mean()
st.write("A média da expectativa de vida dos países que possuem a média de gastos maior que 65 é: {:.2f}" .format(mediaExpectativaMaiorPaises65))

st.write('Conclusão da pergunta 2:')
st.write("Os dados mostram que os países com expectativa de vida maior que 65 anos tendem a apresentar uma média maior de gasto com saúde (% do PIB), " \
"sugerindo que o investimento em saúde pública pode estar associado a uma maior expectativa de vida.")
st.write('\n')


st.subheader('3. Como as taxas de mortalidade infantil e adulta afetam a expectativa de vida?')


st.subheader('4. A expectativa de vida tem correlação positiva ou negativa com hábitos alimentares, estilo de vida, exercícios, fumo, consumo de álcool etc.')
# Alcohol
correlacaoAlcoolMortalidadeAdulta = df[['Alcohol', 'Adult Mortality']].corr()
st.write("O coeficiente de correlação entre o consumo de alcool e a taxa de mortalidade adulta é: ")
st.write(correlacaoAlcoolMortalidadeAdulta)

correlacaoAlcoolMortalidadeInfantil = df[['Alcohol', 'infant deaths']].corr()
st.write("O coeficiente de correlação entre o consumo de alcool e a taxa de mortalidade infantil é: ")
st.write(correlacaoAlcoolMortalidadeInfantil)

# Hepatitis B
correlacaoHepatitisAdulto = df[['Hepatitis B', 'Adult Mortality']].corr()
st.write("O coeficiente de correlação entre a Hepatitis B   e a taxa de mortalidade adulta é: ")
st.write(correlacaoHepatitisAdulto)

correlacaoHepatitisInfantil = df[['Hepatitis B', 'infant deaths']].corr()
st.write("O coeficiente de correlação entre a Hepatitis B e a taxa de mortalidade infantil é: ")
st.write(correlacaoHepatitisInfantil)

st.write('Conclusões da pergunta 4:')
st.write('As correlações entre o consumo de alcool e a hepatitis b com as mortalidades adulta e infantil mostram que' \
' esses hábitos não influenciam diretamente na taxa de mortalidade. ' \
'Todavia, esses dados não demonstram que o alcool não tem nenhum impacto na saude, apenas que não tem correlação direta.')
st.write('\n')


st.subheader('5. Qual é o impacto da escolaridade na expectativa de vida dos seres humanos?')
correlacaoEscolaridadeExpectativa = df[['Schooling', 'Life expectancy']].corr()
st.write("A correlação entre a escolaridade e a expectativa de vida é: ")
st.write(correlacaoEscolaridadeExpectativa)

fig1, ax1 = plt.subplots()
sns.scatterplot(x='Schooling', y='Life expectancy', data=df, ax=ax1)
plt.title("Dispersão entre a escolaridade e a expectativa de vida")
plt.xlabel("Escolaridade")
plt.ylabel("Expectativa de vida")
plt.xlim(-4, 20)
st.pyplot(fig1)

st.write("Conclusões da pergunta 5:")
st.write("Com base no coeficiente entre a expectativa de vida e a escolaridade, percebe-se que, " \
"o coeficiente esta próximo de 1, ou seja, quando a escolaridade aumenta a expectativa tambem aumenta, " \
"demonstrando que um maior investimento na educação ajuda no crescimento da expectativa de vida.")


st.subheader("6. A expectativa de vida tem relação positiva ou negativa com o consumo de álcool? ")

correlacaoAlcoolMortalidadeAdulta = df[['Alcohol', 'Adult Mortality']].corr()
st.write("O coeficiente de correlação entre o consumo de alcool e a taxa de mortalidade adulta é: ")
st.write(correlacaoAlcoolMortalidadeAdulta)

correlacaoAlcoolMortalidadeInfantil = df[['Alcohol', 'infant deaths']].corr()
st.write("O coeficiente de correlação entre o consumo de alcool e a taxa de mortalidade infantil é: ")
st.write(correlacaoAlcoolMortalidadeInfantil)

st.write('Conclusões da pergunta 6:')
st.write('Com base nos coeficientes demonstradas a cima, quanto mais proximo do negativo, menos ligação entre as variáveis exite. Portanto é evidente que o alcool não tem ligação direta com a expectativa de vida. '
'OBS: mesmo com dados lineares, não é possível alegar que o alcool não faz mal ao ser humano!')
st.write('\n')