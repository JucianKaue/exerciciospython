
from time import sleep


def sorteia(n, list):
    from random import randint
    print('¬'*23)
    print(f'Sorteando {n} valores... ')
    for c in range(0, n):
        n = randint(0, 99)
        print(f'\033[33m{n}\033[0m', end=' ')
        list.append(n)
        sleep(0.5)
    print()
    print('¬'*23)


def somaPar(num):
    soma = 0
    print('~' * (29 + len(num)*3))
    print(f'Os \033[33m{len(num)}\033[0m valores inseridos são: ', end='')
    for v in numeros:
        print(f'\033[33m{v:<3}\033[0m', end='')
        if v % 2 == 0:
            soma += v
        sleep(0.5)
    print()
    print(f'A soma dos valores pares é \033[32m{soma}\033[0m')
    print('~' * (29 + len(num)*3))


numeros = []
sorteia(5, numeros)
somaPar(numeros)
