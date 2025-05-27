import csv

contLine = 0
somaPreco = 0
valorTotal = 0

menor = 99999
maior = -99999

contagemProdutos = {}
linhaMaior = {}

listaProdutos = []

with open('estudandoPython/CSV/vendas.csv', mode='r', encoding='utf-8', newline='') as vendas:
    leitura = csv.reader(vendas, delimiter=',')
    
    header = next(leitura)
    print("Cabeçalho encontrado: {}" .format(header))
    
    for linha in leitura:
        ordenado = dict(zip(header, linha))
        
        quantidade = float(ordenado['quantidade'])
        preco = float(ordenado['preco'])
        produto = ordenado['produto']
        
        contLine += 1
        
        # Imprimir todos os dados formatados
        print("Data: {} | Produto: {} | Quantidade: {} | Preço: {}" .format(ordenado['data'], ordenado['produto'], ordenado['quantidade'], ordenado['preco']))
        
        # Imprimir apenas o nome do produto e o preco dele
        print("Produto: {} | Preço: {}" .format(ordenado['produto'], ordenado['preco']))
        
        # Somar todos os valores da coluna preço
        preco = float(ordenado['preco'])
        somaPreco += preco
        
        # Soma o valor total (quantidade * preco)

        valorTotal = (quantidade * preco)
        print("O valor total da venda é: {:.2f}" .format(valorTotal))
        
        # Contar a quantidade de vezes que cada produto aparece
        if (produto in contagemProdutos):
            contagemProdutos[produto] += 1
        else:
            contagemProdutos[produto] = 1
        
        # Somar todos os preços
        somaPreco += preco
        
        # Ver qual é o maior e o menor quantidade vendida
        if (preco > maior):
            maior = preco
        elif (preco < menor):
            menor = preco
            
        # Criar lista de dicionário por linha
        dicionario = dict(zip(header, linha))
        listaProdutos.append(dicionario)

print("A média dos preços é: {:.2f}" .format(float(somaPreco / contLine)))
print("A maior preço vendido é: {} \n O menor preço vendido é: {}" .format(maior, menor))
            
# Gravando todas as linhas em outro arquivo onde o preco é maior que 100   
with open('estudandoPython/CSV/vendas.csv', mode='r', encoding='utf-8', newline='') as vendas:
    leitura = csv.reader(vendas, delimiter=',')
    
    header = next(leitura)
    
    with open('alto_valor.csv', mode='w', encoding='utf-8', newline='') as altasVendas:
        arquivo = csv.writer(altasVendas)
        
        arquivo.writerow(header)
        for linha in leitura:
            if float(linha[3]) > 100:
                arquivo.writerow(linha)
                
print(linhaMaior)
print("O arquivo possui {} linhas" .format(contLine))
print("A soma dos valores da coluna dos preços é: {}" .format(contagemProdutos))

print(listaProdutos)