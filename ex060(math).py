from math import factorial
print('=-'*8, '\033[1mFATORIAL', '-='*8)
n = int(input('Escreva um número para saber seu fatorial: '))
print('O fatorial de {} é {}'.format(n, factorial(n)))
