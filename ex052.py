s = 0
n = int(input('Escreva um numero inteiro: '))
for m in range(1, n+1):
    if n % m == 0:
        s += 1
if s == 2:
    print('O número foi divisivel {} vezes\nO número {} \033[1;32mÉ PRIMO'.format(s, n))
else:
    print('O número foi divisivel {} vezes\nO número {} \033[1;31mNÃO É PRIMO'.format(s, n))
