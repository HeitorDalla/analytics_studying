pessoas = [['Joao', 7, 8], ['Maria', 3, 10], ['Roberta', 10, 6]]

medias = []

for pessoa in pessoas:
    media =  sum(pessoa[1:]) / len(pessoa[1:])
    medias.append(media)

medias.sort(reverse=True)

print(medias)