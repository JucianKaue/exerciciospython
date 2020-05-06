from datetime import datetime
dados = dict()
dados['Nome'] = str(input('Nome: ')).strip().lower().title()
dados['Idade'] = int(datetime.today().year) - int(input('Ano de nascimento: '))
dados['CTPS'] = int(input('Numero da carteira de trabalho (0, caso não tiver): '))
if dados['CTPS'] != 0:
    dados['Contratação'] = int(input('Ano contratação: '))
    dados['Salário'] = int(input('Salário: '))
    dados['Aposentadoria'] = dados['Idade'] + (35 - (datetime.today().year - dados['Contratação']))
print('_-'*25)
for k, v in dados.items():
    print(f'O campo \033[32m{k}\033[0m tem valor \033[33m{v}\033[0m')
