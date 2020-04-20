nome = str(input('Digite o seu nome: ')).strip().title()
print('Seu primeiro nome é {}'.format(nome.split()[0]))
print('Seu último nome é {}'.format(nome.split()[len(nome.split())-1]))
