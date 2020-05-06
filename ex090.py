pessoas = {'nome': str(input('Nome do aluno: ')).strip().title(), 'média': float(input('Média do aluno: '))}
print('\033[36m_-\033[0m'*10)
for k, v in pessoas.items():
    print(f'{k.title()} é igual a {v}')
if pessoas['média'] >= 7:
    print(f'Situação: \033[1;32mAPROVADO\033[0m')
else:
    print(f'Situação: \033[1;31mREPROVADO\033[0m')
