sexo = str(input('Informe o sexo (M/F): ')).strip().upper()
while not sexo in 'MF':
    sexo = input('Dados inválidos, informe o seu sexo:\n').strip().upper()[0]
print('Sexo cadastrado com sucesso')
