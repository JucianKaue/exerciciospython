n1 = int(input('Escreva o primeiro número inteiro: '))
n2 = int(input('Escreva o segundo número inteiro: '))
n3 = int(input('Escreva o terceiro número inteiro: '))
n4 = int(input('Escreva o quarto número inteiro: '))
numeros = (n1, n2, n3, n4)
print('\033[32m_-\033[0m'*20)
v9 = numeros.count(9)
v3 = numeros.count(3)
print(f'Você digitou os valores \033[32m{numeros}\033[0m')
if v9 == 0:
    print('O número 9 não apareceu nenhuma vez')
elif v9 == 1:
    print(f'O número 9 apareceu \033[36m{v9}\033[0m vez')
else:
    print(f'O número 9 apareceu \033[36m{v9}\033[0m vezes')
if v3 == 0:
    print('O número 3 não aparece')
else:
    print(f'O número 3 aparece na \033[33m{numeros.index(3) + 1}\033[0mª posição')
pares = 0
for n in numeros:
    if n != 0:
        if n % 2 == 0:
            pares += 1
print(f'Foram digitados \033[32m{pares}\033[0m números pares sendo eles: \033[32m', end='')
for n in numeros:
    if not n == 0:
        if n % 2 == 0:
            print(n, end=' ')
