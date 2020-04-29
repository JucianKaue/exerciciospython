count = 0
num = list()
while True:
    count += 1
    n = int(input(f'Escreva o \033[33m{count}º\033[0m numero: '))
    if n not in num:
        num.append(n)
    while True:
        opcao = input('Quer continuar? [S/N] ').upper().strip().title()[0]
        if opcao in 'SN':
            break
    if opcao == 'N':
        break
print('='*30)
print(f'Foram digitados \033[32m{count}\033[0m números')
print('Os números em ordem descente são: ', end='')
num.sort(reverse=True)
for c in range(len(num)):
    if c == len(num)-1:
        print(f'\033[32m{num[c]}\033[0m')
    else:
        print(f'\033[32m{num[c]}\033[0m', end=' \033[33m->\033[0m ')
if num.count(5) == 0:
    print('O número 5 não aparece \033[32mnenhuma vez\033[0m')
elif num.count(5) == 1:
    print(f'O número 5 aparece apenas \033[32muma vez\033[0m')
else:
    print(f'O número 5 aparece \033[32m{num.count(5)}\033[0m vezes')

