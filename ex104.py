def leiaInt(msg):
    while True:
        n = input(msg)
        if n.isnumeric():
            break
        print('\033[31mERRO! Digite um número inteiro\033[0m')
    return n


# Programa Principal
n = leiaInt('Digite um número: ')
print(f'Você digitou o valor {n}')
