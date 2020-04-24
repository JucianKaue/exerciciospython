stop = 's'
count = soma = 0
while stop in 'Ss':
    n = float(input('Escreva um número: '))
    stop = input('Quer continuar? ').split()[0]
    while stop not in 'SsNn':
        stop = input('Valor inválido, responda novamente\nQuer continuar? ')
    count += 1
    soma += n
    if count == 1:
        menor = maior = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
media = soma / count
print('A média entre os {} números digitados é {:.2f}'.format(count, media))
print('O maior número digitado foi {}'.format(maior))
print('O menor número digitado doi {}'.format(menor))
