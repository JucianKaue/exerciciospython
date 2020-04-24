count = homens = mulheres = pessoas = 0
while True:
    print('-'*29)
    print('     CADASTRE UMA PESSOA')
    print('-'*29)
    count +=1
    print(f'Insira os dados da {count}ª pessoa: ')
    while True:
        s = str(input('Sexo [M\F]: ')).lower().strip()[0]
        if s in 'mf':
            sexo = s
            break
        else:
            print('Verifique o valor inserido')
    idade = int(input('Idade: '))
    while True:
        continuar = str(input('Quer continuar? [S/N] ')).strip().lower()[0]
        if continuar in 'sn':
            break
    if sexo == 'm':
        homens += 1
    if sexo == 'f' and idade < 20:
        mulheres += 1
    if idade > 18:
        pessoas += 1
    if continuar == 'n':
        print('-_'*24)
        print('RESULTADOS')
        break
print(f'{pessoas} pessoas foram cadastradas com mais de 18 anos')
print(f'{homens} homens foram cadastrados')
print(f'{mulheres} mulheres com menos de 20 anos foram cadastradas')
