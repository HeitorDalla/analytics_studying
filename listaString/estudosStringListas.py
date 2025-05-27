# Lista (array)

listaExemplo = [1, 23, 57, 1, 24, 5]

print(listaExemplo)

# Métodos de uma lista

# Adicionar elementos
listaExemplo.append(23)
print(listaExemplo)

# Adicionar elementos pelo índice
listaExemplo.insert(0, 56) # No índice 0 eu adicionei o elemento 56
print(listaExemplo)

# Adicionar VALORES de outra lista à uma lista
listaExemplo.extend([1, 2, 3])
print(listaExemplo)

# Remove o ELEMENTO especificado
listaExemplo.remove(2)
print(listaExemplo)

# Remove o ULTIMO ELEMENTO ou o INDICE do ELEMENTO espeficicado
listaExemplo.pop()
print(listaExemplo)
#ou
listaExemplo.pop(0)
print(listaExemplo)

# Reverter a ordem da sua lista
listaExemplo.reverse()
print(listaExemplo)

# Ordenar a sua lista
listaExemplo.sort()
print(listaExemplo)

# Limpar toda a lista
listaExemplo.clear()
print(listaExemplo)


# Strings
string = 'heitor dalla villa'

# Split - RETORNA uma LISTA
teste = string.split(' ')
print(teste)

# Join - RECEBE LISTA e RETORNA STRING
frase = ' '.join(teste)
print(frase)

# Strip - Remove os espaços em branco ou caracteres
texto = '   - Heitor Giussani Dalla Villa -   '
print(texto)
textoAlterado = texto.strip()
print(textoAlterado)
