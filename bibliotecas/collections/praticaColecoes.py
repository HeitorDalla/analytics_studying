import csv
from collections import Counter
from collections import defaultdict

produtos = [] # Lista para usar-lo posteriormente para ver a frequência de cada produto

maisVendido = -99999 # Usado para comparação de maiores valores

precosProdutos = defaultdict(list) # Usado para ver todos os preços de cada produto

somaQuantidade = defaultdict(int) # Usado para ver a quantidade total de vendas do produto

valoresOrdenar = [] # Usado para ordenar as maiores quantidades dos produtos vendidos

with open('estudandoPython/bibliotecas/collections/vendas.csv', mode='r', encoding='utf-8', newline='') as vendas:
    leitura = csv.reader(vendas)
    header = next(leitura)

    for linha in leitura:
        ordem = dict(zip(header, linha))
        
        produto = ordem['produto']
        preco = ordem['preco']
        quantidade = ordem['quantidade']
        
        # Adicionar todos os produtos dentro de uma lista para fazer a contagem
        produtos.append(produto)
        
        # Soma do total vendido por produto
        somaQuantidade[produto] += int(quantidade)
        
        # Agrupar todos os precos da venda de cada produto
        precosProdutos[produto].append(float(preco))
        
# Frequência de cada produto vendido
quantidadeProdutos = Counter(produtos)
print(quantidadeProdutos)

# Produto mais vendido
print(quantidadeProdutos.most_common(1))

# Lista de Preços dos produtos
print(precosProdutos)

# Soma para ver a quantidade total vendida por produto
print(somaQuantidade)

# Ordenando os valores da maior quantidade vendida para o menor
for quantidade in somaQuantidade.values():
    valoresOrdenar.append(quantidade)

valoresOrdenados = sorted(valoresOrdenar, reverse=True)
print(valoresOrdenados)

# Lista contendo somente as vendas em que a quantidade foi maior do que 5
listaMaiorCinco = []

with open('estudandoPython/bibliotecas/collections/vendas.csv', mode='rt', encoding='utf-8', newline='') as vendas:
    leitura = csv.reader(vendas)
    
    cabecalho = next(leitura)
    
    for linha in leitura:
        with open('estudandoPython/bibliotecas/collections/maior5.csv', mode='wt', encoding='utf-8', newline='') as maior5:
            arquivo = csv.writer(maior5)
            
            arquivo.writerow(cabecalho)
            
            for linha in leitura:
                if (float(linha[2]) > 5):
                    arquivo.writerow(linha)

# Crie um dicionário que mapeia o produto para o número de vendas distintas.
contagemProdutos = defaultdict(int) # Dicionário onde cada produto vai ter um conjunto de vendas diferentes

with open('estudandoPython/bibliotecas/collections/vendas.csv', mode='rt', encoding='utf-8', newline='') as vendas:
    leitura = csv.DictReader(vendas)
    
    for linha in leitura:
        produto = linha['produto']
        
        contagemProdutos[produto] += 1
        
print(contagemProdutos)

# Usar o Counter para contar quantas vezes cada data aparece no arquivo
contagemData = []

with open('estudandoPython/bibliotecas/collections/vendas.csv', mode='rt', encoding='utf-8', newline='') as vendas:
    leitura = csv.DictReader(vendas)
    
    for linha in leitura:
        data = linha['data']
        
        contagemData.append(data)

# Contagem para saber quantas vezes cada data aparece
contagem = Counter(contagemData)

for d in contagem.items():
    print(d)