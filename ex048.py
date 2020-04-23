soma = 0
count = 0
for x in range(1, 501, +2):
    if x % 3 == 0:
        soma += x
        count += 1
print('A soma de todos os {} valores é {}'.format(count,soma))
