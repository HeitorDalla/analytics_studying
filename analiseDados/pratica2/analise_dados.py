import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

df = pd.read_csv('clientes - clientes.csv', sep=',', encoding='utf-8')

clientesCancelados = df[df['Categoria'] == 'Cancelado']

st.subheader("Análise por Distribuição salarial")
# Histograma - Distribuição de frequência pela faixa salarial
fig1, ax1 = plt.subplots()
ax1.hist(clientesCancelados['Faixa Salarial Anual'], bins=10)
ax1.set_title("Distribuição de Salários dos clientes Cancelados")
ax1.set_xlabel("Salário")
ax1.set_ylabel("Frequência")
st.pyplot(fig1)
st.write("Com base na análise da distribuição salarial dos clientes que cancelaram o cartão, é notório que quanto mais baixo o salário anual, maior a probabilidade do cancelamento acontecer.")
st.write("\n")

st.subheader("Análise por Quantidade de Transações")
# Faixa salarial por Qtde Transacoes 12m
fig2, ax2 = plt.subplots(figsize=(12, 4))
sns.countplot(x='Faixa Salarial Anual', hue='Qtde Transacoes 12m', data=clientesCancelados, ax=ax2)
ax2.set_title("Clientes cancelados por Faixa salarial e Qtde Transacoes 12m")
ax2.set_xlabel("Faixa Salarial Anual")
ax2.set_ylabel("Contagem")
st.pyplot(fig2)
st.write("Pessoas com menor renda apresentam maior volume de transações, o que pode indicar uso mais frequente do cartão, talvez por necessidade ou falta de alternativas de crédito.")
st.write("\n")

st.subheader("Análise por Produtos Contratados")
# Categoria de Cartao por Produtos Contratado
fig3, ax3 = plt.subplots(figsize=(12, 4))
sns.countplot(x='Categoria Cartão', hue='Produtos Contratados', data=clientesCancelados, ax=ax3)
ax3.set_title("Clientes cancelados por Categoria Cartão e Produtos Contratados")
ax3.set_xlabel("Categoria Cartão")
ax3.set_ylabel("Contagem")
st.pyplot(fig3)
st.write("Ao analisar o gráfico, é possivel ver que a maioria dos cancelamentos ocorre com quem tem o cartão blue. Isso sugere que os clientes com planos mais básicos estão propensos a comprar contratar menos produtos, e com isso, estão mais propensos com o cancelamento da conta.")
st.write("\n")

st.subheader("Análise por Dependentes")
# Dependentes por faixa salarial
fig4, ax4 = plt.subplots(figsize=(12, 4))
sns.countplot(x='Dependentes', hue='Faixa Salarial Anual', data=clientesCancelados, ax=ax4)
ax4.set_title("Dependentes por faixa salarial")
ax4.set_xlabel("Dependentes")
ax4.set_ylabel("Contagem")
st.pyplot(fig4)
st.write("Analisando o gráfico, é possível observar que muitas pessoas que cancelaram suas contas possuem mais de 2 dependentes, levando ao pensamento que a pressão familiar existe, levando ao cancelamento da conta.")
st.write("\n")

st.subheader("Plano de Ação")
st.markdown("""
- Clientes com **menor faixa salarial**, **muitos dependentes**, **categoria de cartão básica (blue)** e **baixa diversidade de produtos contratados** tendem a cancelar mais.
- Recomendamos:
  - Oferecer **benefícios personalizados** para clientes da base Blue.
  - Criar **campanhas de engajamento** para clientes com menor uso.
  - Oferecer **educação financeira** como diferencial.
""")