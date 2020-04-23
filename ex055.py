menor = 0
maior = 0
for m in range(1, 6):
    peso = float(input('Escreva o peso da {}ª pessoa: '.format(m)))
    if m == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso é {}'.format(maior))
print('O menor peso é {}'.format(menor))
