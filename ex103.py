def ficha(jogador='n', gols=0):
    if jogador == '':
        jogador = '<não informado>'
    if gols == '':
        gols = 0
    return f'O jogador {jogador} fez {gols} gol(s)'


#Programa Principal
print('¬' * 25)
j = input('Nome do jogador: ').strip().title()
g = input('Quantidade de gols: ')
print(ficha(j, g))
print('¬' * 25)
