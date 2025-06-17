lista = [14, 6, 1, 8, 3, 5]

n = len(lista)
for i in range(n):
    for j in range(0, n - 1 - i):
        if lista[j] > lista[j + 1]:
            lista[j], lista[j + 1] = lista[j + 1], lista[j]
print(lista)