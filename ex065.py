stop = 's'
count = 0
soma = 0
while stop in 'Ss':
    n = float(input('Escreva um número: '))
    stop = input('Quer continuar? ')
    count += 1
    soma += n
    if count == 1:
        maior = n
        menor = n
    if n > maior:
        maior = n
    if n < menor:
        menor = n
m = soma / count
print('A média entre os {} números digitados é {:.2f}'.format(count, m))
print('O maior número digitado foi {}'.format(maior))
print('O menor número digitado doi {}'.format(menor))
