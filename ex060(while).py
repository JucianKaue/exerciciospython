print('=-'*8, '\033[1mFATORIAL', '-='*8)
n = int(input('Escreva um número para saber seu fatorial: '))
fatorial = n
num = n
while not n == 1:
    n -= 1
    fatorial *= n
print('O fatorial de {} é {}'.format(num, fatorial))
