dados = {}
print('='*40)
dados['Nome'] = input('Nome do jogador: ').strip().lower().title()
dados['Partidas'] = int(input(f'Quantidade de partidas jogadas por {dados["Nome"]}: '))
gols = []
for c in range(dados['Partidas']):
    gols.append(int(input(f'-> Quantidade de gols na {c+1}º partida: ')))
    dados['gols'] = gols
dados['total de gols'] = sum(gols)
print('\033[36m_-\033[0m'*40)
print(dados)
print('\033[36m_-\033[0m'*40)
for k, v in dados.items():
    print(f'O campo \033[32m{k}\033[0m tem o valor \033[32m{v}\033[0m')
print('\033[36m_-\033[0m'*40)
print(f'\033[33mO jogador \033[1m{dados["Nome"]}\033[0;33m jogou {dados["Partidas"]} partidas\033[0m')
for c in range(dados['Partidas']):
    print(f'  --> Na {c+1}º partida, {dados["Nome"]} fez {dados["gols"][c]} gols')
