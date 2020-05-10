def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO, Digite um número inteiro válido\033[0m')
        else:
            return n


def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except ValueError:
            print('\033[31mERRO, Digite um número decimal válido\033[0m')
        else:
            return n


i = leiaint('Escreva um número inteiro: ')
f = leiafloat('Escreva um número decimal: ')
print('='*60)
print(f'Você escreveu o búmero inteiro \033[32m{i}\033[0m e o número decimal foi \033[32m{f}\033[0m')
