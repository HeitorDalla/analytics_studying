import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

df = pd.read_csv('bibliotecas/streamlit/pratica1/dados_alunos_escola.csv', sep=',', encoding='utf-8')

st.title("Dados estatísticos para análise fundamentada")

# Estatísticas Descritivas

# Cálculos de Matemática
st.subheader("Estatísticas da matéria de matemática")

mediaMatematica = df['nota_matematica'].mean()
st.write("A média das notas de matemática: {:.2f}" .format(mediaMatematica))

medianaMatematica = df['nota_matematica'].median()
st.write("A mediana das notas de matemática: {}" .format(medianaMatematica))

modaMatematica = df['nota_matematica'].mode()
st.write("A moda das notas de matemática: {}" .format(modaMatematica))

varianciaMatematica = df['nota_matematica'].var()
st.write("A variância das notas de matemática: {:.2f}" .format(varianciaMatematica))

amplitudeMatematica = df['nota_matematica'].max() - df['nota_matematica'].min()
st.write("A amplitude das notas de matemática: {}" .format(amplitudeMatematica))

desvioPadraoMatematica = df['nota_matematica'].std()
st.write("O desvio padrão das notas de matemática: {:.2f}" .format(desvioPadraoMatematica))

# Cálculos de Português
st.subheader("Estatísticas da matéria de português")

mediaPortugues = df['nota_portugues'].mean()
st.write("A média das notas de português: {:.2f}" .format(mediaPortugues))

medianaPortugues = df['nota_portugues'].median()
st.write("A mediana das notas de português: {}" .format(medianaPortugues))

modaPortugues = df['nota_portugues'].mode()
st.write("A moda das notas de português: {}" .format(modaPortugues))

varianciaPortugues = df['nota_portugues'].var()
st.write("A variância das notas de português: {:.2f}" .format(varianciaPortugues))

amplitudePortugues = df['nota_portugues'].max() - df['nota_portugues'].min()
st.write("A amplitude das notas de português: {}" .format(amplitudePortugues))

desvioPadraoPortugues = df['nota_portugues'].std()
st.write("O desvio padrão das notas de português: {:.2f}" .format(desvioPadraoPortugues))


# Cálculos de Ciências
st.subheader("Estatísticas da matéria de ciências")

mediaCiencias = df['nota_ciencias'].mean()
st.write("A média das notas de ciências: {:.2f}" .format(mediaCiencias))

medianaCiencias = df['nota_ciencias'].median()
st.write("A mediana das notas de ciências: {}" .format(mediaCiencias))

modaCiencias = df['nota_ciencias'].mode()
st.write("A moda das notas de ciências: {}" .format(modaCiencias))

varianciaCiencias = df['nota_ciencias'].var()
st.write("A variância das notas de ciências: {:.2f}" .format(varianciaCiencias))

amplitudeCiencias = df['nota_ciencias'].max() - df['nota_ciencias'].min()
st.write("A amplitude das notas de ciências: {}" .format(amplitudeCiencias))

desvioPadraoCiencias = df['nota_ciencias'].std()
st.write("O desvio padrão das notas de ciências: {:.2f}" .format(desvioPadraoCiencias))


# Frequência média dos alunos por série e construir gráfico representando
frequenciaAlunos = df.groupby('serie')['frequencia_%'].mean()

st.subheader("A frequência média dos alunos por série: \n")
st.write(frequenciaAlunos)


# Filtros e Agrupamentos

# Filtre os alunos com frequência abaixo de 75% e calcule a média geral deles
mediaAlunosAbaixo75 = df.loc[df['frequencia_%'] < 75]
st.write("A média dos alunos com frequência menor que 75% é: {:.2f}\n" .format(mediaAlunosAbaixo75['frequencia_%'].mean()))

# Use groupby para obter a nota média por cidade e matéria
mediaMatematica = df.groupby('cidade')['nota_matematica'].mean()
mediaPortugues = df.groupby('cidade')['nota_portugues'].mean()
mediaCiencias = df.groupby('cidade')['nota_ciencias'].mean()

st.subheader("A média da nota de matemática por cidades é: \n")
st.write(mediaMatematica)
st.subheader("A média da nota de português por cidades é: \n")
st.write(mediaPortugues)
st.subheader("A média da nota de ciencias por cidades é: \n")
st.write(mediaCiencias)

# Crie a seguinte classificação:
#a. Nota menor que 3,0 = reprovado
#b. Nota menor que 6,0 = exame
#c. Nota acima de 6,0 = aprovado

st.subheader("A classificação por média dos alunos é: ")
df['media'] = (df['nota_matematica'] + df['nota_portugues'] + df['nota_ciencias']) / 3

df['classificacao'] = df['media'].apply(lambda media: 'REPROVADO' if media <= 3 else 'EXAME' if media < 6 else 'APROVADO')

st.write(df[['nome', 'media', 'classificacao']])

# Quantos alunos possuem a nota menor que 3,0
menor3 = df.loc[df['media'] < 3].value_counts()
st.write("{} alunos ficaram abaixo de 3". format(menor3.count()))

# Quantos alunos possuem a nota menor que 5,0
menor5 = df.loc[(df['media'] >= 3) & (df['media'] < 5)].value_counts()
st.write("{} alunos ficaram abaixo de 5". format(menor5.count()))

# Quantos alunos possuem a nota menor que 7,0
menor7 = df.loc[(df['media'] >= 5) & (df['media'] < 7)].value_counts()
st.write("{} alunos ficaram abaixo de 7". format(menor7.count()))

# Quantos alunos possuem a nota menor que 9,0
menor9 = df.loc[(df['media'] >= 7) & (df['media'] < 9)].value_counts()
st.write("{} alunos ficaram abaixo de 9". format(menor9.count()))

# Quantos alunos possuem a nota igual a 10,0
menor10 = df.loc[df['media'] == 10].value_counts()
st.write("{} alunos ficaram igual a 10\n". format(menor10.count()))

# Qual cidade tem a melhor nota em Matemática, português e ciências? E a Pior nota?
cidadeMaiorNotaMat = df.sort_values('nota_matematica', ascending=False)

st.subheader("As maiores e menores notas de cada matéria: ")

st.write("Matemática")

st.write("A maior nota de matematica é a cidade: {}" .format(cidadeMaiorNotaMat['cidade'].head(1).squeeze()))
st.write("A menor nota de matematcia é a cidade: {}" .format(cidadeMaiorNotaMat['cidade'].tail(1).squeeze()))

st.write("Português")

cidadeMaiorNotaPort = df.sort_values('nota_portugues', ascending=False)
st.write("A maior nota de portugues é a cidade: {}" .format(cidadeMaiorNotaPort['cidade'].head(1).squeeze()))
st.write("A menor nota de portugues é a cidade: {}" .format(cidadeMaiorNotaPort['cidade'].tail(1).squeeze()))

st.write("Ciências")

cidadeMaiorNotaCien = df.sort_values('nota_ciencias', ascending=False)
st.write("A maior nota de ciencias é a cidade: {}" .format(cidadeMaiorNotaCien['cidade'].head(1).squeeze()))
st.write("A menor nota de ciencias é a cidade: {}" .format(cidadeMaiorNotaCien['cidade'].tail(1).squeeze()))


# Visualizações

st.subheader("Visualização das notas por matéria")

# Notas de Matemática
fig1, ax1 = plt.subplots()
plt.hist(x=df['nota_matematica'], bins=20)
plt.title("Visualização da nota de matemática")
plt.xlabel("Nota")
plt.ylabel("Frequência")
st.pyplot(fig1)

# Notas de Português
fig2, ax2 = plt.subplots()
plt.hist(x=df['nota_portugues'], bins=20)
plt.title("Visualização da nota de portugues")
plt.xlabel("Nota")
plt.ylabel("Frequência")
plt.show()
st.pyplot(fig2)

# Notas de Ciências
fig3, ax3 = plt.subplots()
plt.hist(x=df['nota_ciencias'], bins=20)
plt.title("Visualização da nota de ciencias")
plt.xlabel("Nota")
plt.ylabel("Frequência")
plt.show()
st.pyplot(fig3)

# Gere um boxplot comparando notas de português por série
st.subheader("Notas de cada matéria por série")

fig4, ax4 = plt.subplots()
sns.boxplot(x='nota_matematica', y='serie', data=df, ax=ax4)
plt.title("Notas de matemática por série")
plt.show()
st.pyplot(fig4)

# Gere um boxplot comparando notas de matemática por série
fig5, ax5 = plt.subplots()
sns.boxplot(x='nota_portugues', y='serie', data=df, ax=ax5)
plt.title("Notas de português por série")
plt.show()
st.pyplot(fig5)

# Gere um boxplot comparando notas de ciências por série
fig6, ax6 = plt.subplots()
sns.boxplot(x='nota_ciencias', y='serie', data=df, ax=ax6)
plt.title("Notas de ciências")
plt.show()
st.pyplot(fig6)

# Crie um gráfico de barras com a quantidade de alunos por cidade
st.subheader("Quantidade de alunos por cidade")

fig7, ax7 = plt.subplots()
sns.countplot(x='cidade', data=df, ax=ax7)
plt.title("Frequência de alunos por cidade")
plt.xlabel("Cidade")
plt.ylabel("Quantidade de Alunos")
plt.xticks(rotation=45)
plt.show()
st.pyplot(fig7)

# Faça um gráfico de dispersão entre frequencia_% e nota por matéria
st.subheader("Gráfico de frequência por matéria")

fig8, ax8 = plt.subplots()
sns.scatterplot(x='frequencia_%', y='nota_matematica', data=df, ax=ax8)
plt.title("Dispersão por nota de matemática")
plt.show()
st.pyplot(fig8)

fig9, ax9 = plt.subplots()
sns.scatterplot(x='frequencia_%', y='nota_portugues', data=df, ax=ax9)
plt.title("Dispersão por nota de portugues")
plt.show()
st.pyplot(fig9)

fig10, ax10 = plt.subplots()
sns.scatterplot(x='frequencia_%', y='nota_ciencias', data=df, ax=ax10)
plt.title("Dispersão por nota de ciencias")
plt.show()
st.pyplot(fig10)