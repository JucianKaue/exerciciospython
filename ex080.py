num = list()
for count in range(1, 6):
    n = (int(input(f'Escreva o {count}º valor: ')))
    if count == 1 or n > max(num):
        num.append((n))
        print('Valor adinicionado no \033[32mfinal da lista\033[0m')
    else:
        pos = 0
        while True:
            if n <= num[pos]:
                num.insert(pos, n)
                print(f'Valor inserido na \033[32m{pos+1}ª posição da lista\033[0m')
                break
            pos += 1
print('\033[35m_-\033[0m'*27)
print('A lista em ordem crescente é: ', end='')
for p, e in enumerate(num):
    if p == len(num)-1:
        print(f'\033[32m{e}\033[0m')
    else:
        print(f'\033[32m{e}\033[0m', end=' -> ')