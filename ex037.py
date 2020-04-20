n = int(input('Escreva o numero que deseja converter: '))
print('''Escolha uma das bases de conversão:
( 1 ) Para converter para BINÁRIO
( 2 ) Para converter para OCTAL
( 3 ) Para converter para HEXADECIMAL''')
opcao = int(input('Escolha uma opção: '))
if opcao == 1:
    print('O numero {} convertido para BINÁRIO é {}'.format(n,bin(n)[2:]))
elif opcao == 2:
    print('O número {} convertido para OCTAL é {}'.format(n,oct(n)[2:]))
elif opcao == 3:
    print('O número {} convertido para HEXAGONAL é {}'.format(n,hex(n)[2:]))
else:
    print('ERRO\nO numero {} não está entre as opções'.format(opcao))
