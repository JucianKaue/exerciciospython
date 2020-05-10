from time import sleep
from ex115 import *

try:
    abrir()
except:
    criar()
while True:
    while True:
        menu()
        o = leiaint('O que você deseja fazer? ')
        if o in '123':
            o = int(o)
            break
    if o == 1:
        titulo('pessoas cadastradas')
        pessoas = ler_pessoas()
        sleep(1)
    elif o == 2:
        titulo('adicionar pessoas')
        sleep(0.3)
        nome = input('Nome: ')
        idade = leiaint('Idade: ')
        adicionar(nome, idade)
    elif o == 3:
        titulo('fechando o programa')
        sleep(1)
        print('<<\033[32mVOLTE SEMPRE\033[0m>>'.center(45))
        sleep(1)
        break
