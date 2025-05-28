produto = (('Laptop', 10, 'R$ 1500'))

# Fatiamento
print("O nome do produto é: {}" .format(produto[0]))
print("A quantidade de estoque do produto {} é: {}" .format(produto[0], produto[1]))
print("O preco do produto {} é: {}" .format(produto[0], produto[1]))
print("O produto e quantidade existente da tupla é: {}" .format(produto[:2]))
print("Pulando de dois em dois vai ser: {}" .format(produto[::2]))
print("Pulando de um em um vai ser: {}" .format(produto[::1]))

# Transformando as tuplas em lista e vice versa
lista = list(produto)
print("Aqui esta a tupla que foi transformada em lista: {}" .format(lista)) # Agora eu posso modifica-la como eu quiser

# Adicionando produtos
lista.append(['Computador', 20, 4000])
print("A lista atualizada é: {}" .format(lista))

# Transformando em tupla novamente
tuplaVolta = tuple(lista)
print("A lista que foi transformado em tupla novamente é: {}" .format(tuplaVolta))

# Tentativa de mudar algum item da tupla
tuplaTeste = (1, 2, 3, 4, 5)

try:
    tuplaTeste[0] = 10
except:
    print("Deu erro")

print("Mas eu estou aqui")

# Esse exemplo mostra a importância do tratamento de erros, pois sem ele, o programa ia parar no 'Deu erro'.
# Mesmo exemplo sem o tratamento de erros
tuplaTeste2 = (1, 2, 3, 4, 5)

tuplaTeste[0] = 10

print("Deu erro")

print("Mas eu estou aqui")