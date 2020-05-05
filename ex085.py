print('='*10, '\033[32mANALIZADOR DE NÚMEROS\033[0m', '='*10)
numeros = [[], []]
for c in range(1, 8):
    n = int(input(f'Escreva o {c}º número: '))
    if n % 2 == 0:
        numeros[0].append(n)
    else:
        numeros[1].append(n)
numeros[0].sort()
numeros[1].sort()
print('\033[35m_-\033[0m'*20)
print('Os números pares são: ', end='')
for e in numeros[0]:
    print(f'\033[32m{e}\033[0m', end=' ')
print('\nOs números impares são: ', end='')
for e in numeros[1]:
    print(f'\033[32m{e}\033[0m', end=' ')
