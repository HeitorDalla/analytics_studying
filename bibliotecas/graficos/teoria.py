import pandas as pd
import matplotlib.pyplot as plt

# Passo a passo para montar os dados

# 1 - Preparar os dados
x = [1, 2, 3, 4]
y = [11, 22, 33, 44]

# 2 - Montar o modelo orientado a objetos
fig, ax = plt.subplots(figsize=(10, 10))

# 3 - Colocar os dados no gráfico
ax.plot(x, y)

# 4 - Personalizar o gráfico
ax.set(title='Grafico simples',
       xlabel='x-axis',
       ylabel='y-axis')

# 5- Salvar o gráfico
fig.savefig('imagens/simples_grafico.png')