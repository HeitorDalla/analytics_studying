import csv
from datetime import date, time, datetime, timedelta
from collections import defaultdict

datasDatetime = []

dataAtual = date.today()
diaAtual = dataAtual.day
listDiferenca = []

ultimosDias = timedelta(days=30)
listUltimosDias = []

vendasPorMes = defaultdict(list) # Agrupar as vendas por mês

vendasMaio = []

# Converter a string da coluna data (YYYY-MM-DD) em objetos datatime
with open('estudandoPython/bibliotecas/datetime/vendas.csv', mode='rt', encoding='utf-8', newline='') as vendas:
    leitor = csv.DictReader(vendas)
    
    for linha in leitor:
        data = linha['data']
        
        # Convertendo todas as datas em objetos datetime
        dataConvertida = datetime.strptime(data, "%Y-%m-%d")
        datasDatetime.append(dataConvertida)
        
        # Pegando a diferença de dias de cada data das vendas para o dia atual
        dataVenda = dataConvertida.date()
        diferençaDia = dataAtual - dataVenda
        listDiferenca.append(diferençaDia)
        
        # Pegando todas as vendas que aconteceram nos ultimos 30 dias     
        if (diferençaDia.days < 30):
            listUltimosDias.append(linha)
            
        # Agrupando as vendas por mês
        anoMes = dataConvertida.strftime("%m/%Y")
        vendasPorMes[anoMes].append(linha)
        
        # Filtrando as vendas de maio
        if (anoMes == '05/2025'):
            vendasMaio.append(linha)
          
# Imprimindo todas as datas em objetos datetime      
for data in datasDatetime:
    print(data)
    
# Imprimindo a diferença de cada data com a data atual
for dia in listDiferenca:
    print("A diferença de dias foi de: {}" .format(dia))

# Imprimindo todas as vendas que ocorreram nos ultimos 30 dias
for venda in listUltimosDias:
    print(data)

# Imprimindo as vendas agrupados por mês
for mes, vendas in vendasPorMes.items():
    print(f"\nMês: {mes} - {len(vendas)} venda(s)")
    for venda in vendas:
        print(f"  - {venda}")

# Imprimindo as vendas de maio
for venda in vendasMaio:
    print(venda)