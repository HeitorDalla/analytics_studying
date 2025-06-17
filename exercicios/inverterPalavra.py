string = 'teste para string'

stringSemEspaco = string.replace(' ', '')

print(stringSemEspaco)

listaString = list(stringSemEspaco)

listaString.reverse()

print(listaString)

stringJuntada = ''.join(listaString)

print(stringJuntada)