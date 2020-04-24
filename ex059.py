from time import sleep
opcao = 0
n1 = float(input('Escreva um valor: '))
n2 = float(input('Escreva outro valor: '))
print('O que você quer fazer?')
while not opcao == 5:
    print('\033[1m[1] somar\n[2] multiplicar\n[3] maior\n[4] inserir novos números\n[5] sair do programa\033[0m')
    opcao = input('')
    if opcao == '':
        print('Valor inválido, tente novamente')
        print('O que você quer fazer?')
    else:
        opcao = int(opcao)
        if opcao == 1:
            if n1 == int(n1) and n2 == int(n2):
                print('{:.0f} + {:.0f} = {:.0f}'.format(n1, n2, n1+n2))
            else:
                print('{} + {} = {}'.format(n1, n2, n1+n2))
        elif opcao == 2:
            if n1 == int(n1) and n2 == int(n2):
                print('{:.0f} x {:.0f} = {:.0f}'.format(n1, n2, n1*n2))
            else:
                print('{} x {} = {}'.format(n1, n2, n1*n2))
        elif opcao == 3:
            if n1 > n2:
                print('{} é maior que {}'.format(n1, n2))
            elif n1 < n2:
                print('{} é maior que {}'.format(n2, n1))
            else:
                print('Os números são iguais')
        elif opcao == 4:
            n1 = float(input('Escreva um valor: '))
            n2 = float(input('Escreva outro valor: '))
            print('O que você quer fazer?')
        elif opcao == 5:
            print('Saindo',end='')
            for n in range(0,3):
                print('.', end='')
                sleep(0.5)
        elif opcao == '':
            print('nada')
        else:
            print('Valor inválido')
