from time import sleep
print('\033[32m='*17, 'TABUADA', '='*17, '\033[0m')
print('\033[31mse quiser parar escreva um número negativo\033[0m')
while True:
    print('-_'*15)
    n = int(input('Você deseja ver qual tabuada? '))
    if n < 0:
        break
    for m in range(1, 11):
        print(f'{n} x {m} = {n*m}')
        sleep(0.3)
