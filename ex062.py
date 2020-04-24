from time import sleep
count = 0
r = True
print('='*21)
print('PROGRASSÃO ARITMÉTICA')
print('='*21)
termo_1 = int(input('Primeiro termo da PA: '))
razao = int(input('Razão da progressão aritmética: '))
n = 10
while not count == n:
    count += 1
    termo_1 += razao
    print(termo_1, end=' ')
    sleep(0.3)
    if count == n:
        n +=int(input('\nvocê deseja continuar por mais quantas vezes? '))
print('Progressão finalizada com {} termos'.format(count))
