eleicao = {}

for i in range(4):
    pessoa = input("Digite o nome do candidato em que voce deseja votar: (Alice, Bob, Charlie): ")
    
    if pessoa in eleicao:
        eleicao[pessoa] += 1
    else:
        eleicao[pessoa] = 1
        
pessoaVotada = ''
maiorVoto = -1

print("Resultados: ")

for nome, votos in eleicao.items():
    print("{}: {} votos" .format(nome, votos))
    
    if (votos > maiorVoto):
        maiorVoto = votos
        pessoaVotada = nome

print("O vencedor é: {}" .format(pessoaVotada))