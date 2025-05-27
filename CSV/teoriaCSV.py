# Trabalhando com arquivos csv
import csv

# open('vendas.csv', …) - abre o arquivo chamado vendas.csv. (Posso especificar um caminho também)
# mode='r' - abre o arquivo em modo leitura
# encoding='utf-8' - especidica o conjunto de caracteres usados para ler o arquivo de texto
# newline='' - evita problemas de quebras de linha duplicadas ao usar o módulo csv
# with … as f: - garante que o arquivo será fechado automaticamente ao sair deste bloco 

with open('CSV/vendas.csv', mode='r', encoding='utf-8', newline='') as f:
    
    # Crie um leitor CSV que separa cada linha por vírgula
    leitor = csv.reader(f, delimiter=',')
    
    # Ler a primeira linha do cabeçalho para obter os nomes das colunas
    header = next(leitor)
    print("Cabeçalho encontrado: {}" .format(header))
    
    # Percorrer cada linha restante do arquivo csv
    for linha in leitor:
        
        # zip(header, linha) - Emparelha cada nome de coluna com o valor correspondente da linha, criando pares como ('produto','camisa')
        # dict(...) - converte esses pares em um dicionário, por exemplo
        
        ordem = dict(zip(header, linha))
        print("Produto: {} | Quantidade: {} | Preço: {}" .format(ordem['produto'], ordem['quantidade'], ordem['preco']))