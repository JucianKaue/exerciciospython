def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except ValueError:
            print('\033[31mERRO, Digite um número inteiro válido\033[0m')
        else:
            return n
            break


def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except ValueError:
            print('\033[31mERRO, Digite um número decimal válido\033[0m')
        else:
            return n
            break


i = leiaint('Escreva um número inteiro: ')
f = leiafloat('Escreva um número decimal: ')
print('='*30)
print(f'Você escreveu os números {i} e {f}')
