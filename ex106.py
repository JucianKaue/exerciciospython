from time import sleep


def titulo(msg, cod_cor=0, cor_fundo=0):
    t = len(msg) + 4
    print(f'\033[{cod_cor};{cor_fundo}m¬\033[0m'*t)
    print(f'\033[{cod_cor};{cor_fundo}m{msg:^{t}}\033[0m')
    print(f'\033[{cod_cor};{cor_fundo}m¬\033[0m'*t)


while True:
    titulo('SISTEMA DE AJUDA PyHELP', 30, 43)
    f = input('\033[0mDigite a função ou a biblioteca para ver seu manual: ').strip().lower()
    if f == 'fim':
        titulo('Encerrando', 30, 41)
        break
    titulo(f'Mostrando manual de "{f}"', 30, 45)
    sleep(1)
    print('\033[44m')
    help(f)
    print('\033[0m')
    sleep(1)
