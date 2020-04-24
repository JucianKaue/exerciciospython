from random import randint
n = 15
count = 0
num = randint(1, 10)
print('_-'*6, 'Vamos brincar?', '-_'*6, '\nEstou pensando em um número entre 1 e 10')
print('Tente adivinhar: ', end='')
while not num == n:
    count += 1
    n = int(input(''))
    if num != n:
        print('\033[1;31mERROOU\033[0m')
        print('Tente novamente: ', end='')
print('\033[1;32mACERTOU\033[0m\nParabéns, você precisou de {} tentativas'.format(count))

