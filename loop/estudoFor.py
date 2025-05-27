lista = [1, 2, 34, 523, 7, 9, 1, 90]

# Imprime a posição
for i in lista:
    print(i)
    
print("----------------------------")
    
# Imprime o índice
for i in range(len(lista)):
    print(i)
    
print("----------------------------")

# Imprime o índice e o valor
for i, v in enumerate(lista):
    print(i, v)