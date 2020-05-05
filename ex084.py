pessoas = []
p = []
peso = []
while True:
    p.append(str(input('Nome: ').strip().title()))
    p.append(float(input('Peso: ')))
    pessoas.append(p[:])
    peso.append(p[1])
    p.clear()
    while True:
        r = input('Quer continuar? [S/N] ').strip().title()[0]
        if r in 'SN':
            break
    if r == 'N':
        break
pesadas = []
leves = []
for c in range(len(pessoas)):
    if pessoas[c][1] == max(peso):
        pesadas.append(pessoas[c])
    if pessoas[c][1] == min(peso):
        leves.append(pessoas[c])
print('='*30)
print(f'Foram cadastradas \033[33m{len(pessoas)} pessoas\033[0m')
print('As pessoas mais pesadas são: ')
for c in range(len(pesadas)):
    print(f'\033[31m{pesadas[c][0]} com {pesadas[c][1]} Kg\033[0m')
print('As pessoas mais leves são: ')
for c in range(len(leves)):
    print(f'\033[32m{leves[c][0]} com {leves[c][1]} Kg\033[0m')
