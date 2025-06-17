palavras = ['cachorro', 'gato', 'lebre', 'zebra', 'urubu']

tamanhos = {}

def organizarPalavras (lista):
    for palavra in lista:
        tamanho = len(palavra)

        if tamanho not in tamanhos:
            tamanhos[tamanho] = palavra
        else:
            tamanhos[tamanho] += ", {}" .format(palavra)
    
    return tamanhos


resultado = organizarPalavras(palavras)

for tamanho, palavra in resultado.items():
    print(tamanho, palavra)