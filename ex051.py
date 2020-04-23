print('\033[1m='*29, '\033[0m')
print('10 PRIMEIROS TERMOS DE UMA \033[1mPA')
print('\033[1m='*29, '\033[0m')
primeiro = int(input('Primeiro termo da progressão: '))
razao = int(input('Razão da progressão aritmética: '))
for m in range(0, 11):
    pa = primeiro + (m * razao)
    print(pa, end=' ')
