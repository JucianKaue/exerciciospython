print('--/'*5, 'FATORIAL', '/--'*5)
n = int(input('Escreva um número para saber seu fatorial: '))
fatorial = n
for count in range(n-1, 0, -1):
    fatorial *= count
print('O fatorial de {} é {}'.format(n, fatorial))
