n1 = int(input('Escreva um numero inteiro: '))
n2 = int(input('Escreva outro numero: '))
if n1>n2:
    print('O primeiro numero (\033[1;32m{}\033[0m) é maior.'.format(n1))
elif n2>n1:
    print('O segundo numero (\033[1;32m{}\033[0m) é maior.'.format(n2))
else:
    print('Os dois numeros são iguais.')
