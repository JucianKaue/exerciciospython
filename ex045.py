import random
import emoji
print(emoji.emojize(':curling_stone::paperclip::scissors:'*4))
print('\033[1;34;46m  PEDRA, PAPEL, TESOURA  \033[0m')
print(emoji.emojize(':curling_stone::paperclip::scissors:'*4))
e = str(input('\033[1;46mVenha jogar comigo!!\033[0m\nEscolha: '))
escolha = e.strip().lower()
a = random.choice(['pedra','papel','tesoura'])
print('O compuatador jogou \033[1m{}'.format(a))
if a=='pedra':
    if 'papel' in escolha:
        print('\033[1;32mParabéns! Você ganhou.')
    elif 'pedra' in escolha:
        print('\033[1;33mEmpate')
    elif 'tesoura' in escolha:
        print('\033[1;31mVocê Perdeu!')
    else:
        print('\033[1;30;41mERRO\033[0m')
elif a=='papel':
    if 'tesoura' in escolha:
        print('\033[1;32mParabéns! Você ganhou.')
    elif 'papel' in escolha:
        print('\033[1;33mEmpate')
    elif 'pedra' in escolha:
        print('\033[1;31mVocê Perdeu!')
    else:
        print('\033[1;30;41mERRO\033[0m')
elif a=='tesoura':
    if 'pedra' in escolha:
        print('\033[1;32mParabéns! Você ganhou.')
    elif 'tesoura' in escolha:
        print('\033[1;33mEmpate')
    elif 'papel' in escolha:
        print('\033[1;31mVocê Perdeu!')
    else:
        print('\033[1;30;41mERRO\033[0m')
