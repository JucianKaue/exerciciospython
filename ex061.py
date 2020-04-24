from time import sleep
count = 0
print('='*15, '10 PRIMEIROS TERMOS DE UMA PA', '='*15)
p1 = int(input('Primeiro termo da PA: '))
r = int(input('Razão da PA: '))
print('Os 10 primeiros números dessa PA são:')
while not count == 10:
    count += 1
    pa = p1 + r
    p1 += r
    print(pa, end=' ')
    sleep(0.5)
