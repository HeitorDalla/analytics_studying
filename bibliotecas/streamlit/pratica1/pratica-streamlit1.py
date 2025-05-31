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