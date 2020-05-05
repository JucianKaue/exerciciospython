numeros = [[], [], [], [], []]
soma_par = soma_coluna = 0
for x in range(0, 3):
    for y in range(0, 3):
        n = int(input(f'Escreva um número para a posição [{x}, {y}]: '))
        numeros[x].append(n)
        if n % 2 == 0:
            numeros[3].append(n)
print('\033[1;32m-_\033[0m'*20)
for e in range(0, 3):
    for c in range(0, 3):
        print(f'[ {numeros[e][c]} ]', end='')
        if c == 2:
            soma_coluna += numeros[e][c]
        if e == 1:
            numeros[4].append(numeros[e][c])
    print()
for c in numeros[3]:
    soma_par += c
print('\033[1;32m-_\033[0m'*20)
print(f'A soma de todos os números pares é {soma_par}')
print(f'A soma dos números da terceira coluna é {soma_coluna}')
print(f'O maior número da segunda linha é {max(numeros[4])}')
