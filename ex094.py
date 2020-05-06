pessoas = dict()
temp = dict()
mulheres = []
idosos = []
count = s_idade = 0
while True:
    count += 1
    print('<'*10, f'\033[32m{count}º pessoa\033[0m', '>'*10)
    temp['nome'] = str(input('Nome: ')).strip().lower().title()
    while True:
        temp['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
        if temp['sexo'] in 'MF':
            break
        print('ERRRO! Responda apenas M ou F')
    temp['idade'] = int(input('Idade: '))
    while True:
        r = input('Quer continuar? [S/N] ').strip().upper()[0]
        if r in 'SN':
            break
        print('ERRO! Responda apenas S ou N')
    pessoas[f'pessoa{count}'] = temp.copy()
    temp.clear()
    if r == 'N':
        break
print('\033[35m_-\033[0m'*25)
print(f'Foram cadastradas {len(pessoas)} pessoas')
for p in range(len(pessoas)):
    s_idade += pessoas[f"pessoa{p+1}"]["idade"]
print(f'A média de idade é {s_idade / count:.2f} anos')
for p in range(len(pessoas)):
    if pessoas[f'pessoa{p+1}']['sexo'] == 'F':
        mulheres.append(pessoas[f'pessoa{p+1}'].copy())
    if pessoas[f'pessoa{p+1}']['idade'] >= s_idade / count:
        idosos.append(pessoas[f'pessoa{p+1}'].copy())
print('\033[32m-\033[0m'*50)
print('Mulheres: ')
print(f'\033[33m{"NOME":<10}{"SEXO":<10}{"IDADE":<10}\033[0m')
for m in range(len(mulheres)):
    for k, v in mulheres[m].items():
        print(f'{v:<10}', end=' ')
    print()
print('\033[32m-\033[0m'*50)
print('As pessoas com idade acima da média são:')
print(f'\033[33m{"NOME":<10}{"SEXO":<10}{"IDADE":<10}\033[0m')
for m in range(len(idosos)):
    for k, v in idosos[m].items():
        print(f'{v:<10}', end=' ')
    print()
