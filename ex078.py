num = list()
for c in range(1, 6):
    num.append(int(input(f'Escreva o {c}º valor: ')))
print('-_'*26)
print(f'Os números digitados são: \033[32m{num}\033[0m')
print(f'O maior valor digitado é \033[32m{max(num)}\033[0m que está nas posições ', end='')
for p, n in enumerate(num):
    if n == max(num):
        print(f'\033[33m{p + 1}\033[0m', end=', ')
print(f'\nO menor valor digitado é \033[32m{min(num)}\033[0m que está nas pisições ', end='')
for p, n in enumerate(num):
    if n == min(num):
        print(f'\033[33m{p + 1}\033[0m', end=', ')
