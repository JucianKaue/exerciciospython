def ficha(jogador='', gols=''):
    if jogador == '':
        jogador = '<não informado>'
    if gols.isnumeric():
        gols = int(gols)
    else:
        gols = 0
    return f'O jogador \033[33m{jogador}\033[0m fez \033[33m{gols}\033[0m gol(s)'


#Programa Principal
print('¬' * 40)
j = input('Nome do jogador: ').strip().title()
g = input('Quantidade de gols: ')
print(ficha(j, g))
print('¬' * 40)
