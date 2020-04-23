import datetime
ano_atual = datetime.date.today().year
maioridade = 0
menoridade = 0
for m in range(1, 8):
    nascimento = int(input('Escreva o ano de  da {}ª pessoa: '.format(m)))
    idade = ano_atual - nascimento
    if idade >= 18:
        maioridade += 1
    else:
        menoridade += 1
print('{} são maiores de idade\n{} são menores de idade'.format(maioridade, menoridade))
