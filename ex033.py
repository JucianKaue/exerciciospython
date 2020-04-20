n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo Numero: '))
n3 = int(input('Terceiro número: '))
if n1>n2>n3:
    print('O maior numero é {}, e o menor é {}.'.format(n1,n3))
elif n1>n3>n2:
    print('O maior numero é {}, e o menor é {}.'.format(n1,n2))
elif n2>n1>n3:
    print('O maior numero é {}, e o menor é {}.'.format(n2,n3))
elif n2>n3>n1:
    print('O maior numero é {}, e o  menor é {}.'.format(n2,n1))
elif n3>n2>n1:
    print('O maior numero é {}, e o menor é {}.'.format(n3,n1))
elif n3>n1>n2:
    print('O maior numero é {}, e o menor é {}.'.format(n3,n2))
else:
    print('Todos os numeros são iguais.')
