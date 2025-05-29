# Trabalhando com valores padrões
# Para colocar valores por padrão (0), não precisando criar a chave
from collections import defaultdict

vendas_tuplas = [('camisa',3), ('calça',2), ('camisa',1)]

# Soma - para soma em cada produto a quantidade vendida
somaVendas = defaultdict(int) # Cria o defaultdict que retorna 0 para chaves novas

for produto, quantidade in vendas_tuplas:
    somaVendas[produto] += quantidade # Se produto não existir, vira 0 + qtd

print(somaVendas)


# Agrupando os valores por cliente, usando uma lista como padrão
from collections import defaultdict

pedidos = [
    ('Ana',    'camisa'),
    ('Bruno',  'calça'),
    ('Ana',    'boné'),
    ('Ana',    'chinelo'),
    ('Ana',    'vestido'),
    ('Bruno',    'camisa')
]

agrupamento = defaultdict(list)

for cliente, produto in pedidos:
    agrupamento[cliente].append(produto)
    
print(dict(agrupamento))