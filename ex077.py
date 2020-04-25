palavras = ('Celular', 'Borracha', 'Corretivo', 'Fone', 'Mouse', 'Computador', 'Segurança', 'Monitor', 'Pen Drive', 'Carregador', 'Python')
for palavra in palavras:
    print(f'Palavra: \033[32m{palavra:10}\033[0m', end=' ')
    print('Vogais: ', end='')
    for l in palavra:
        if l.lower() in 'aeiou':
            print(f'\033[31m{l.upper()}\033[0m', end=' ')
    print('')
