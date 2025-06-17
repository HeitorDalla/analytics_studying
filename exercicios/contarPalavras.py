frase = 'Teste para ver quantas palavras tem na frase'

def contarPalavras (f):
    resultado = f.strip().split()
    
    return len(resultado)

resultado = contarPalavras(frase)

print("Sua frase tem {} palavras." .format(resultado))