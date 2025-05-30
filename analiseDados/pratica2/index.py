import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

df = pd.read_csv("analiseDados/pratica2/Life_Expectancy_Data.csv", sep=',', encoding='utf-8')

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


st.subheader('1. Os vários fatores de previsão inicialmente escolhidos realmente afetam a expectativa devida?', divider='grey')

numeric_df = df.select_dtypes(include='number')
correlation = numeric_df.corr()['Life expectancy'].sort_values(ascending=False)

st.write("Maiores correlações positivas com expectativa de vida:")
st.write(correlation)

st.write("Quais variáveis realmente afetam a expectativa de vida?")
st.write("Schooling anos de estudo: Educação está diretamente ligada a melhores condições de vida e saúde.")
st.write("Polio / Diphtheria / Hepatitis B (vacinação): Alta cobertura vacinal previne doenças e eleva a expectativa de vida.")
st.write("GDP per capita: PIB per capita mais alto geralmente reflete mais investimento em saúde e bem-estar.")
st.write("BMI (IMC médio da população): Indica boa nutrição em níveis adequados.")

st.write('Conclusão da pergunta 1:')
st.write("Os dados demonstram que diversos fatores de previsão influenciam significativamente a expectativa de vida. " \
"Ao calcular a correlação de Pearson entre essas variáveis e a expectativa de vida, observa-se tanto relações positivas quanto negativas. " \
"Isso indica que certas variáveis estão fortemente associadas a aumentos ou reduções na longevidade da população")
st.write('\n')


st.subheader('2. Um país com menor expectativa de vida (<65) deve aumentar seus gastos com saúde para melhorar sua expectativa de vida média?', divider='grey')

# Média da expectativa de vida dos países que tem a média de expectativa de vida menor que 65
# Expectativa de vida ao longo dos anos
porPais = df.groupby('Country')['Life expectancy'].mean().sort_values()
menor65 = porPais[porPais < 65]

menor65Linhas = df[df['Country'].isin(menor65.index)].copy()

menor65Linhas['percentage expenditure'] = (
    menor65Linhas['percentage expenditure']
    .str.replace('.', '')
    .str.replace(',', '.')
    .astype(float)
)

fig, ax = plt.subplots()
sns.lineplot(x='Year', y='Life expectancy', data=df, legend=False, ax=ax)
plt.title("Espectativa de vida por país ao longo dos anos")
plt.xlabel("Ano")
plt.ylabel("Espectativa de vida")
st.pyplot(fig)

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


st.subheader('3. Como as taxas de mortalidade infantil e adulta afetam a expectativa de vida?', divider='grey')

correlacaoMortalidadeAdultaExpectativa = df[['Life expectancy', 'Adult Mortality']].corr()
st.write("O coeficiente de correlação entre a expectativa de vida e a taxa de mortalidade adulta é: ")
st.write(correlacaoMortalidadeAdultaExpectativa)

fig1, ax1 = plt.subplots()
sns.regplot(x='Adult Mortality', y='Life expectancy', data=df, ax=ax1)
plt.title("Dispersão a mortalidade adulta e a expectativa de vida")
plt.xlabel("Mortalidade adulta")
plt.ylabel("Expectativa de vida")
st.pyplot(fig1)

correlacaoMortalidadeInfantilExpectativa = df[['Life expectancy', 'infant deaths']].corr()
st.write("O coeficiente de correlação entre a expectativa de vida e a taxa de mortalidade infantil é: ")
st.write(correlacaoMortalidadeInfantilExpectativa)

fig2, ax2 = plt.subplots()
sns.regplot(x='Life expectancy', y='infant deaths', data=df, ax=ax2)
plt.title("Dispersão entre a expectativa de vida e a mortalidade infantil")
plt.xlabel("Life expectancy")
plt.ylabel("Mortalidade infantil")
st.pyplot(fig2)

st.write('Conclusão da pergunta 3:')
st.write("As taxas de mortalidade infantil e adulta tem correlação negativas com a expectativa de vida, ou seja, " \
"quanto maiores as taxas de mortalidade, menor tende a ser a expectativa.")
st.write('\n')


st.subheader('4. A expectativa de vida tem correlação positiva ou negativa com hábitos alimentares, estilo de vida, exercícios, fumo, consumo de álcool etc.', divider='grey')

# Alcool
correlacaoAlcoolExpectativaVida = df[['Alcohol', 'Life expectancy']].corr()
st.write("O coeficiente de correlação entre o consumo de alcool e a expectativa de vida é: ")
st.write(correlacaoAlcoolExpectativaVida)

fig1, ax1 = plt.subplots()
sns.regplot(x='Alcohol', y='Life expectancy', data=df, ax=ax1)
plt.title("Dispersão entre o consumo de alcool e a expectativa de vida")
plt.xlabel("Alcool")
plt.ylabel("Expectativa de vida")
st.pyplot(fig1)

# Desnutrição dos 1-19 anos
correlacaoDesnutricaoExpectativaVida = df[['thinness  1-19 years', 'Life expectancy']].corr()
st.write("O coeficiente de correlação entre a desnutrição dos 1-19 anos e a expectativa de vida é: ")
st.write(correlacaoDesnutricaoExpectativaVida)

fig3, ax3 = plt.subplots()
sns.regplot(x='thinness  1-19 years', y='Life expectancy', data=df, ax=ax3)
plt.title("Dispersão entre a Desnutrição dos 1-19 anos e a expectativa de vida")
plt.xlabel("Desnutrição dos 1-19 anos")
plt.ylabel("Expectativa de Vida")
st.pyplot(fig3)

st.write('Conclusão da pergunta 4:')
st.write("A expectativa de vida tem pouca relação com o alcool, porém, muita correlação com a desnutrição." \
"Bons hábitos alimentares tem impactos significativos na expectativa de vida.")
st.write('\n')


st.subheader('5. Qual é o impacto da escolaridade na expectativa de vida dos seres humanos?', divider='grey')

correlacaoEscolaridadeExpectativa = df[['Schooling', 'Life expectancy']].corr()
st.write("A correlação entre a escolaridade e a expectativa de vida é: ")
st.write(correlacaoEscolaridadeExpectativa)

fig5, ax5 = plt.subplots()
sns.scatterplot(x='Schooling', y='Life expectancy', data=df, ax=ax5)
plt.title("Dispersão entre a escolaridade e a expectativa de vida")
plt.xlabel("Escolaridade")
plt.ylabel("Expectativa de vida")
plt.xlim(-4, 20)
st.pyplot(fig5)

st.write("Conclusões da pergunta 5:")
st.write("Com base no coeficiente entre a expectativa de vida e a escolaridade, percebe-se que, " \
"o coeficiente esta próximo de 1, ou seja, quando a escolaridade aumenta a expectativa tambem aumenta, " \
"demonstrando que um maior investimento na educação ajuda no crescimento da expectativa de vida.")



correlacaoAlcoolExpectativa = df[['Alcohol', 'Life expectancy']].corr()
st.write("A correlação entre a expectativa de vida e o consumo de alcool é: ")
st.write(correlacaoAlcoolExpectativa)

fig6, ax6 = plt.subplots()
sns.regplot(x='Alcohol', y='Life expectancy', data=df, ax=ax6, scatter_kws={"alpha":0.5})
plt.title("Gráfico de dispersão para a expectativa de vida com o consumo de alcool")
plt.xlabel("Alcool")
plt.ylabel("Expectativa de vida")
st.pyplot(fig6)

st.write('Conclusões da pergunta 6:')
st.write('Com base no coeficiente demonstrado a cima, quanto mais proximo do 0, menos ligação entre as variáveis exite. Portanto é evidente que o alcool não tem ligação direta com a expectativa de vida. '
'OBS: mesmo com dados lineares, não é possível alegar que o alcool não faz mal ao ser humano!')
st.write('\n')


st.subheader("7. Países densamente povoados tendem a ter menor expectativa de vida?", divider='grey')

fig7, ax7 = plt.subplots()
sns.regplot(x='Population', y='Life expectancy', data=df, ax=ax7, scatter_kws={"alpha":0.2})
plt.title("Gráfico de dispersão que relaciona a densidade da população e a expectativa de vida")
plt.xlabel("Population")
plt.ylabel("Expectativa de vida")
st.pyplot(fig7)

st.write('Conclusões da pergunta 7:')
st.write('Com base na análise gráfica é possível observar que a densidade demográfica não afeta a expectativa de vida.')
st.write('\n')


st.subheader("8. Qual é o impacto da cobertura de imunização na expectativa de vida?", divider='grey')

fig8, ax8 = plt.subplots(figsize=(8, 6))
sns.regplot(x='Diphtheria', y='Life expectancy', data=df, ax=ax8)
plt.title('Cobertura de Imunização contra Difteria x Expectativa de Vida')
plt.ylabel('Cobertura de Difteria (%)')
plt.ylabel('Expectativa de Vida (anos)')
st.pyplot(fig8)

fig9, ax9 = plt.subplots(figsize=(8, 6))
sns.regplot(x='Polio', y='Life expectancy', data=df, ax=ax9)
plt.title('Cobertura de Imunização contra Polio x Expectativa de Vida')
plt.ylabel('Cobertura de Polio (%)')
plt.ylabel('Expectativa de Vida (anos)')
st.pyplot(fig9)

fig10, ax10 = plt.subplots(figsize=(8, 6))
sns.regplot(x='Hepatitis B', y='Life expectancy', data=df, ax=ax10)
plt.title('Cobertura de Imunização contra Hepatitis B x Expectativa de Vida')
plt.ylabel('Cobertura de Hepatitis B (%)')
plt.ylabel('Expectativa de Vida (anos)')
st.pyplot(fig10)

st.write('Conclusões da pergunta 7:')
st.write('A análise mostra uma correlação positiva entre a cobertura de imunização infantil (Hepatite B, Poliomielite e Difteria) e a expectativa de vida. ' \
'Isso indica que quanto maior o alcance da vacinação em uma população, maior tende a ser a longevidade média das pessoas, ' \
'reforçando a importância de programas nacionais de imunização.')
st.write('\n')