listagem = ('tenis', 35, 'meia', 15, 'pantufa', 20, 'Casaco', 125, 'Camiseta', 50, 'Jaqueta', 80.90, 'Cueca', 10, 'Zorba', 30)
print('='*28)
print('      LISTA DE PREÇOS')
print('='*28)
for count in range(len(listagem)):
    if count % 2 == 0:
        print(f'{listagem[count].title():-<20}', end='R$')
    else:
        print(f'{listagem[count]:>7.2f}')
print('='*28)
