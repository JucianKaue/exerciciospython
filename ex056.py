soma_idade = 0
idade_velho = 0
count_mulheres = 0
for p in range(1, 6):
    print('===== {}ª PESSOA ====='.format(p))
    nome = input('Nome: ').strip().title()
    idade = int(input('Idade: '))
    sexo = input('Sexo (M/F): ').strip().upper()
    if p == 1 and sexo == 'M':
        idade_velho = idade
        nome_velho = nome
    else:
        if idade > idade_velho and sexo == 'M':
            idade_velho = idade
            nome_velho = nome
    if idade < 20 and sexo == 'F':
        count_mulheres += 1
    soma_idade += idade
media_idade = soma_idade / 5
print('\nA média de idade do grupo é {:.1f} anos'.format(media_idade))
print('O nome do homem mais velho é \033[1m{}\033[0m'.format(nome_velho))
print('Este grupo tem {} mulheres com menos de 20 anos'.format(count_mulheres))

