from random import randint
from time import sleep
listas = []
jogo = []
print('='*10, '\033[32mGERADOR DE PALPITES MEGA SENA\033[0m', '='*10)
n = int(input('Quantos jogos você quer gerar? '))
for c in range(0, n):
    for e in range(0, 6):
        n = randint(1, 60)
        while n in jogo:
            n = randint(1, 60)
        jogo.append(n)
    listas.append(jogo[:])
    jogo.clear()
print('\033[36m_-\033[0m'*25)
print(f'\033[33mO sorteando {len(listas)} palpites: \033[0m')
for c in range(len(listas)):
    print(f'Jogo {c+1:>2}: ', end='')
    for e in range(len(listas[c])):
        sleep(0.3)
        print(f'\033[32m{listas[c][e]:^2}\033[0m', end=' ')
    print()
print('<'*5, '  BOA SORTE  ', '>'*5)
