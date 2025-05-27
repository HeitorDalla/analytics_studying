# Fábrica de Funções das Operações Matemáticas

def fabricaOperacoes (n1, n2, o):
    
    def soma (*argumentos):
        soma = 0
        
        for argumento in argumentos:
            soma += int(argumento)
            
        return soma
    
    def subtracao (*argumentos):
        resultado = argumentos[0]
        
        for argumento in argumentos[1:]:
            resultado = resultado - argumento
            
        return resultado
        
    def multiplicacao (*argumentos):
        multiplicacao = 1
        
        for argumento in argumentos:
            multiplicacao *= argumento
            
        return multiplicacao
            
    def divisao (*argumentos):
        resultado = argumentos[0]
        
        for argumento in argumentos[1:]:
            if (argumento == 0):
                return 'Não pode ser dividido por 0!'
            else:
                resultado = resultado / argumento
                
        return resultado
    
    if (o == 'soma'):
        return soma(n1, n2)
        
    elif (o == 'subtracao'):
        return subtracao(n1, n2)
        
    elif (o == 'multiplicacao'):
        return multiplicacao(n1, n2)
        
    elif (o == 'divisao'):
        return divisao(n1, n2)
        
numero1 = int(input("Digite um numero: "))
numero2 = int(input("Digite outro numero numeo: "))
operacao = str(input("Qual operação deseja realizar? [soma/subtracao/multiplicacao/divisao]"))

operacaoRealizar = fabricaOperacoes(numero1, numero2, operacao)

print("O resultado da operacao {} {} e {} é: {}" .format(operacao, numero1, numero2, operacaoRealizar))