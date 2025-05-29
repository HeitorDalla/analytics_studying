# Trabalhando com datas - Para trabalhar e manipulas datas dentro do python, temos que importar o 'datetime'
from datetime import date, time, datetime, timedelta
# date - representa apenas uma data (AAAA-MM-DD)
# time - representa apenas um horário (HH-MM-SS-MIMI)
# datetime - combina (data + hora) em um mesmo objeto
# timedelta - representa uma duração (diferença entre datas/horas)

# Pegando a data atual
hoje = date.today() # Padrão americano (AAAA-MM-DD)
print(hoje)

# Criando um timestamp (data + hora)
agora = datetime.now()
print(agora)

# Criando uma data específica
meuAniversario = date(2006, 7, 6)
print(meuAniversario)

# Converter uma data em string de data
hoje = date.today()
formato = '%d/%m/%Y'
print(hoje.strftime(formato))

# Converter uma string para uma data
dataString = "2025-05-21 14:30"
fomatoNovo = "%Y-%m-%d %H:%M"
dataConvertida = datetime.strptime(dataString, fomatoNovo)
print(dataConvertida)