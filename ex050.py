s = 0
for m in range(0, 6):
    n = int(input('Escreva um número: '))
    if n % 2 == 0:
        s += n
print('A soma entre todos os números pares informados é {}'.format(s))
