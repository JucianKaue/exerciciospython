num = list()
while True:
    n = int(input('Escreva um valor inteiro: '))
    while True:
        opcao = input('Quer continuar? [S/N] ').strip().upper()[0]
        if opcao in 'SN':
            break
    if n not in num:
        print('\033[32mValor adicionado com sucesso!\033[0m')
        num.append(n)
    else:
        print('\033[31mO valor já está na lista\033[0m')
    if opcao == 'N':
        break
print('\033[36m=\033[0m'*60)
print('Os números digitados foram: ', end='')
num.sort()
for count in range(len(num)):
    if count == len(num)-1:
        print(f'\033[32m{num[count]}')
    else:
        print(f'\033[32m{num[count]}', end=' -> ')
