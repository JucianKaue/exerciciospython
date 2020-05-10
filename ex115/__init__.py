def linha():
    print('\033[34m¬\033[0m'*40)


def titulo(msg):
    txt = msg.upper()
    linha()
    print(f'{txt:^40}')
    linha()

def menu():
    linha()
    print(f'\033[32m{"MENU PRINCIPAL":^40}\033[0m')
    titulo('1 - Ver pessoas cadastradas\n'
           '2 - Cadastrar uma nova pessoa\n'
           '3 - Sair')


def abrir():
    arquivo = open('pessoas.txt', 'a')
    arquivo.close()


def criar():
    try:
        arquivo = open('pessoas.txt', 'x')
        arquivo.close()
    except:
        print('Erro na criação do arquivo')


def escrever(txt):
    arquivo = open('pessoas.txt', 'a+')
    conteudo = arquivo.readlines()
    conteudo.append(txt)
    arquivo.write(f'{conteudo}')
    arquivo.close()


def adicionar(nome, idade):
    temp = []
    n = nome.strip().title()
    i = idade
    temp.append(n)
    temp.append(i)
    escrever(f'/{temp[0]};{temp[1]}/')
    temp.clear()


def ler_pessoas():
    from time import sleep
    arquivo = open('pessoas.txt', 'r')
    texto = arquivo.read()
    arquivo.close()
    if texto == '':
        print(f"\033[31m{'NINGUÉM FOI CADASTRADO':^30}\033[0m")
    else:
        txt = texto.split('/')
        nomes = []
        for e in txt:
            if e not in "['" and e not in "']" and e not in "']['":
                nomes.append(e)
        dados = []
        for e in nomes:
            dados.append(e.split(';'))
        print(f'\033[33m{"NOME":^30}|{"IDADE":^10}\033[0m')
        for p in dados:
            print(f'{p[0]:^30}|{p[1]:^10}')
            sleep(0.5)


def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO, Digite um número inteiro válido\033[0m')
        else:
            return str(n)

