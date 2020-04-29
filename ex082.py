num = list()
count = 0
while True:
    count += 1
    n = int(input(f'Escreva o {count}º número: '))
    if n not in num:
        num.append(n)
    while True:
        opcao = input('Quer continuar? (S/N) ').strip().upper()[0]
        if opcao in 'NS':
            break
    if opcao == 'N':
        break
pares = list()
impares = list()
print('\033[36m/\033[0m'*40)
num.sort()
print(f'Os números digitados são: ', end='')
for n in num:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
    print(f'\033[32m{n}\033[0m', end=' ')
pares.sort()
print(f'\nOs numeros pares digitados foram: ', end='')
for p in pares:
    print(f'\033[32m{p}\033[0m', end=' ')
impares.sort()
print(f'\nOs números ímpares digitados foram: ', end='')
for i in impares:
    print(f'\033[32m{i}', end=' ')
