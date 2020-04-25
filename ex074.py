from random import randint
numeros = (randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))
print('Os números sorteados são: \033[33m', end='')
for n in numeros:
    print(n, end=' ')
'''for count, num in enumerate(numeros):
    if count == 0:
        maior = menor = num
    else:
        if maior < num:
            maior = num
        if menor > num:
            menor = num
print(f'\n\033[0mO maior número é: \033[32m{maior}\033[0m')
print(f'O menor número é: \033[31m{menor}')'''
#ou
print(f'\n\033[0mO maior valor sorteado foi \033[32m{max(numeros)}\033[0m')
print(f'O menor valor sorteado foi \033[31m{min(numeros)}')