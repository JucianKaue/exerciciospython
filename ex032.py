from datetime import date
ano = int(input('Escreva o ano que você quer analizar: Se quiser analizar o ano atual digite 0: '))
if ano == 0:
    ano = date.today().year
if ano%4 == 0 and ano % 100 != 0 or ano %400 == 0:
    print('Esse é um ano bissexto.')
else:
    print('Esse não é um ano bissexto.')
