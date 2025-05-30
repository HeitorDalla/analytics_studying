import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

df = pd.read_csv("estudandoPython/bibliotecas/graficos/dados_estatisticas.csv", sep=',', encoding='utf-8')

st.header("Estatísticas das idades e salários")

# Idade: média, moda, mediana, variancia, desvio padrão e aplitude
st.subheader("Estatísticas das idades")

df['idade'].mean()
st.write("A média das idades é: {}" .format(df['idade'].mean()))

df['idade'].mode()
st.write("A moda das idades é: {}" .format(df['idade'].mode()))

df['idade'].median()
st.write("A mediana das idades é: {}" .format(df['idade'].median()))

df['idade'].var()
st.write("A variância das idades é: {}" .format(df['idade'].var()))

df['idade'].std()
st.write("O desvio padrão das idades é: {}" .format(df['idade'].std()))

amplitude = df['idade'].max() - df['idade'].min()
st.write("A amplitude das idades é: {}" .format(amplitude))

df['idade'].describe()
st.write("O resumo geral das idades é: {}\n" .format(df['idade'].describe()))

# Salário: média, moda, mediana, variancia, desvio padrão e aplitude
st.subheader("Estatísticas dos salários")

df['salario'].mean()
st.write("A média dos salario é: {}" .format(df['salario'].mean()))

df['salario'].mode()
st.write("A moda dos salários é: {}" .format(df['salario'].mode()))

df['salario'].median()
st.write("A mediana dos salários é: {}" .format(df['salario'].median()))

df['salario'].var()
st.write("A variância dos salários é: {}" .format(df['salario'].var()))

df['salario'].std()
st.write("O desvio padrão dos salários é: {}" .format(df['salario'].std()))

amplitude = df['salario'].max() - df['salario'].min()
st.write("A amplitude dos salários é: {}" .format(amplitude))

df['salario'].describe()
st.write("O resumo geral dos salários é: {}" .format(df['salario'].describe()))

# Criação de uma nova coluna chamada faixa etária
df['faixa_etaria'] = df['idade'].apply(lambda idade: 'Jovem' if idade <= 25 else 'Adulto' if idade <= 45 else 'Sênior')
st.write("A nova faixa etária para a classificação das pessoas: ")
st.write(df['faixa_etaria'])


# Visualização com gráficos

# Gráfico de barras (countplot) - Usado para contagem por categoria
fig1, ax1 = plt.subplots()
sns.countplot(x='estado', data=df, ax=ax1)
plt.ylabel("Contagem")
plt.title("Distribuição por estado")
plt.show()
st.pyplot(fig1)

# Gráfico de barras (barplot) - Mostra um estimador (média, moda, mediana, soma) agrupado por categoria
fig2, ax2 = plt.subplots()
sns.barplot(x='departamento', y='salario', data=df, hue='estado', estimator=sum, ax=ax2)
plt.title("Salário por departamento")
plt.show()
st.pyplot(fig2)

# Gráfico de (lineplot) - Mostra uma variação contínua de um grupo
fig3, ax3 = plt.subplots()
sns.lineplot(x='idade', y='salario', data=df, hue='departamento', ax=ax3)
plt.show()
st.pyplot(fig3)

# Histograma - Distribuição de frequência
fig4, ax4 = plt.subplots()
plt.hist(df['idade'], bins=15) # Bins - quantas caixas eu quero criar
plt.title("Distribuição de Idades")
plt.xlabel("Idade")
plt.ylabel("Frequência")
plt.show()
st.pyplot(fig4)

# Gráfico de dispersão - Relaçao entre duas variáveis numéricas
fig5, ax5 = plt.subplots()
sns.scatterplot(x='idade', y='salario', hue='departamento', data=df, ax=ax5)
plt.title("Dispersão entre idade e salario")
plt.show()
st.pyplot(fig5)

# Boxplot de salário por departamento - Usado para resumos estatítisticos e outliers (valores atípicos)
fig6, ax6 = plt.subplots()
sns.boxplot(x='departamento', y='salario', data=df, ax=ax6)
plt.title("Salário por departamento")
plt.show()
st.pyplot(fig6)