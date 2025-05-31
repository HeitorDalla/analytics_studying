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

