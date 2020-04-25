brasileirão_2019 = ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Athletico-PR', 'São Paulo', 'Internacional', 'Corinthians', 'Fortaleza',
                    'Goiás', 'Bahia', 'Vasco', 'Athlético-MG', 'Fluminense', 'Botafogo', 'Ceará', 'Cruzeiro', 'Csa', 'Chapecoense', 'Avaí')
linha = '__'*30
time = input('Qual time você torce? ').strip().lower().title()
print(linha)
print(f'Tabela do Brasileirão de 2019: {brasileirão_2019}')
print(linha)
print(f'Os 5 primeiros colocados são: {brasileirão_2019[:5]}')
print(linha)
print(f'Os 4 últimos são: {brasileirão_2019[-4:]}')
print(linha)
print(f'A lista em ordem alfabética é: {sorted(brasileirão_2019)}')
print(linha)
print(f'A chapecoense está na {brasileirão_2019.index("Chapecoense")+1}ª posição')
print(linha)
if time in brasileirão_2019:
    print(f'O seu time é {time} e está na {brasileirão_2019.index(time)+1}ª posição')
else:
    print('Desculpa, não encontramos o seu time na tabela')
