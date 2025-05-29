# Trabalhando com contagens
# Contar quantas vezes algum dado aparece
from collections import Counter

vendas = ['camisa','calça','camisa','boné','calça','camisa', 'cueca', 'calça', 'bone']

quantidadeVendas = Counter(vendas)
print(quantidadeVendas)
print(quantidadeVendas.most_common(1)) # Mostrar qual produto mais aparece