n = 0
s = 0
count = 0
while n != 999:
    n = int(input('Escreva um número: '))
    count += 1
    s += n
print('A soma entre os {} números digitados é {}'.format(count, s-999))
