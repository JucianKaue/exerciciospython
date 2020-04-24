from random import randint
print('\033[36m='*20)
print('   \033[1;32mPAR OU IMPAR\033[0m   ')
print('\033[36m=\033[0m'*20)
acertos = 0
while True:
    print('\033[34m_-\033[0m'*10)
    computador = randint(0, 1)
    jogador = int(input('Numero: '))
    while True:
        opcao = str(input('Par ou impar? ')).strip().upper()[0]
        if opcao in 'PI':
            break
        else:
            print('Erro, tente novamente')
            print('\033[34m_-\033[0m'*10)
    print('-'*21)
    if (jogador + computador) % 2 == 0:
        if opcao == 'P':
            acertos += 1
            print('Parabéns, você \033[32mGANHOU\033[0m')
            print('Vamos brincar denovo!')
        else:
            print('Você \033[31mPERDEU\033[0m')
            print(f'Vitorias consecutivas: {acertos}')
            break
    else:
        if opcao == 'I':
            acertos += 1
            print('Parabéns, você \033[32mGANHOU\033[0m')
            print('Vamos brincar denovo!')
        else:
            print('Você \033[31mPERDEU\033[0m')
            print(f'Vitórias consecutivas: {acertos}')
            break
