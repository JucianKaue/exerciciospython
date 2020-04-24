count_50 = count_20 = count_10 = count_1 = 0
print('\033[1;32m=-'*10)
print('       BANCO')
print('=-'*10, '\033[0m')
valor = int(input('Valor do saque: '))
while True:
    if valor % 50 == 0:
        valor -= 50
        count_50 += 1
    elif valor % 20 == 0:
        valor -= 20
        count_20 += 1
    elif valor % 10 == 0:
        valor -= 10
        count_10 += 1
    elif valor % 1 == 0:
        valor -= 1
        count_1 += 1
    if valor == 0:
        break
print('-'*20)
print(f'{count_50} notas de R$50,00')
print(f'{count_20} notas de R$20,00')
print(f'{count_10} notas de R$10,00')
print(f'{count_1} notas de R$1,00')
print('-'*20)
