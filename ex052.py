s = 0
n = int(input('Escreva um numero inteiro: '))
for m in range(1, n):
    if n % m == 0:
        s = s + 1
if s == 1:
    print('O número {} é número primo'.format(n))
else:
    print('O número {} não é número primo'.format(n))