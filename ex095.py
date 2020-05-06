jogadores = {}
dados = {}
count = 0
while True:
    count += 1
    print('='*10, f'\033[32m{count}º JOGADOR\033[0m', '='*10)
    dados['Numero'] = count
    dados['Nome'] = input('Nome do jogador: ').strip().lower().title()
    dados['partidas'] = int(input(f'Quantidade de partidas jogadas por {dados["Nome"]}: '))
    gols = []
    for c in range(dados['partidas']):
        gols.append(int(input(f'Quantidade de gols na {c+1}º partida: ')))
        dados['gols'] = gols
    tot_gols = 0
    for c in gols:
        tot_gols += c
    dados['total_gols'] = tot_gols
    jogadores[f'jogador{count}'] = dados.copy()
    dados.clear()
    while True:
        r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if r in 'SN':
            break
    if r == 'N':
        break
print('_='*37)
print(f'{"NÚMERO":<15}{"NOME":<15}{"PARTIDAS":<15}{"GOLS":<15}{"TOTAL DE GOLS":<15}')
print('-'*74)
for c in range(len(jogadores)):
    for j in jogadores[f'jogador{c+1}'].values():
        print(f'{str(j):<15}', end='')
    print()
print('-'*74)
n = int(input('Você quer mostrar os dados de qual jogador? '))
for c in range(jogadores[f'jogador{n}']['partidas']):
    print(f'  --> Na {c+1}º partida, {jogadores[f"jogador{n}"]["Nome"]} fez {jogadores[f"jogador{n}"]["gols"][c]} gols')
