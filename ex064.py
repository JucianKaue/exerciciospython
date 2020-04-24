n = soma = count = 0
n = int(input('Escreva um número (para parar escreva "999"): '))
while n != 999:
    count += 1
    soma += n
    n = int(input('Escreva um número (para parar escreva "999"): '))
print('A soma entre os {} números digitados é {}'.format(count, soma))
