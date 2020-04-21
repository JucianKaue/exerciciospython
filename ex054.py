import datetime
ano_atual = datetime.date.today().year
maioridade = 0
menoridade = 0
for m in range(0,7):
    nascimento = int(input('Escreva seu ano de nascimento: '))
    idade = ano_atual - nascimento
    if idade >= 21:
        maioridade = maioridade + 1
    else:
        menoridade = menoridade + 1
print('{} são maiores de idade e {} são menores de idade'.format(maioridade,menoridade))
