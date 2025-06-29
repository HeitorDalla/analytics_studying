import pandas as pd

# Ler o arquivo vendas.csv
df = pd.read_csv('bibliotecas/pandas/pratica1/vendas.csv', sep=',', encoding='utf-8', parse_dates=['data']) # parse_dates é uma biblioteca do pandas para alterar 'data'

print(df)

# Lendo o total de vendas dentro do meu arquivo
totalVendas = len(df)
print(totalVendas)

# Calculando o faturamento total da planilha de vendas
faturamento = (df['quantidade'] * df['preco']).sum()
print("O faturamento total é de: {:.2f}" .format(faturamento))

# Calcular o valor médio por venda
valorMedioVendas = faturamento / totalVendas
print("O valor médio das vendas é de: {:.2f}" .format(valorMedioVendas))

# Mostrar os 3 produtos mais vendidos
top3 = df['produto'].value_counts().head(3)
print(top3)

# Mostrar as 5 maiores vendas
df['total'] = df['quantidade'] * df['preco']

cincoMaioresVendas = df['total'].nlargest(5)
print("As cinco maiores vendas são: \n{}" .format(cincoMaioresVendas))

# Filtrar apenas as vendas do mês de abril
abril = df.loc[df['data'].dt.month == 4]
relatorio_abril = abril.copy() # Cópia

relatorio_abril.to_csv('bibliotecas/pandas/pratica1/relatorioAbril.csv', index=False)