numeros = [[], [], []]
for x in range(0, 3):
    for y in range(0, 3):
        numeros[x].append(int(input(f'Escreva o valor para a posição [{x}, {y}]: ')))
print('\033[36m=\033[0m'*40)
for x in range(0, 3):
    for y in range(0, 3):
        print(f'[ {numeros[x][y]:^4} ]', end='')
    print()
