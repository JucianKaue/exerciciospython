from time import sleep


def abrir():
    arquivo = open('pessoas.txt', 'a')
    arquivo.close()


def criar():
    arquivo = open('pessoas.txt', 'x')
    arquivo.close()


def escrever(txt):
    arquivo = open('pessoas.txt', 'a+')
    conteudo = arquivo.readlines()
    if not conteudo == '':
        conteudo.append(txt)
        arquivo.write(f'{conteudo}')
    else:
        arquivo.write(f'{txt}\n')
    arquivo.close()


def ler():
    arquivo = open('pessoas.txt', 'r')
    texto = arquivo.read()


def linha():
    print('¬'*30)


def titulo(msg):
    txt = msg.upper()
    linha()
    print(f'{txt:^30}')
    linha()


def cadastro():
    # try:
    abrir()
    '''except:
        criar('pessoas.txt')'''
    while True:
        titulo('menu principal')
        while True:
            titulo('1 - Ver pessoas cadastradas\n'
                  '2 - Cadastrar uma nova pessoa\n'
                  '3 - Sair')
            o = input('O que você deseja fazer? ')
            if o in '123':
                o = int(o)
                break
        if o == 1:
            titulo('pessoas cadastradas')
            pessoas = ler()
        if o == 2:
            titulo('adicionar pessoas')
            temp = []
            nome = input('Nome: ').strip().title()
            idade = input('Idade: ')
            temp.append(nome)
            temp.append(idade)
            escrever(f' {temp[0]} {temp[1]} ')
            temp.clear()
        if o == 3:
            titulo('fechando o programa')
            print('<<VOLTE SEMPRE>>')
            break



cadastro()