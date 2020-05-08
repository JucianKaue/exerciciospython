def titulo(msg, cor_txt=0, cor_fundo=0):
    """
    ->> Escreve uma mensagem em formato de título
    :parametro - msg: Recebe o texto do título
    :parametro - cor_txt: recebe o código da cor do texto, que são:
        - 30 para Branco
        - 31 para Vermelho
        - 32 para Verde
        - 33 para Amarelo
        - 34 para azul
        - 35 para roxo
        - 36 para azul claro
        - 37 para cinza

    :parametro - cor_fundo: Recebe o código da cor do fundo, que são:
        - 40 para Branco
        - 41 para Vermelho
        - 42 para Verde
        - 43 para Amarelo
        - 44 para azul
        - 45 para roxo
        - 46 para azul claro
        - 47 para cinza
    """
    t = len(msg) + 4
    print(f'\033[1;{cor_txt};{cor_fundo}m¬\033[0m'*t)
    print(f'\033[1;{cor_txt};{cor_fundo}m{msg:^{t}}\033[0m')
    print(f'\033[1;{cor_txt};{cor_fundo}m¬\033[0m'*t)


def ajuda(f):
    from time import sleep
    titulo(f'Mostrando manual de "{f}"', 30, 45)
    sleep(1)
    print('\033[7;30m')
    help(f)
    print('\033[0m')


# Programa Principal
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 30, 42)
    f = input('\033[0mDigite a função ou a biblioteca para ver seu manual: ').strip().lower()
    if f == 'fim':
        titulo('Encerrando', 30, 41)
        break
    else:
        ajuda(f)
