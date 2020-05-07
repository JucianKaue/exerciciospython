def contador(a, b, c):
    from time import sleep
    if c == 0:
        c = 1
    if c < 0:
        c *= -1
    print('~'*30)
    print(f'Contando de \033[32m{a}\033[0m até \033[32m{b}\033[0m de \033[32m{c}\033[0m em \033[32m{c}\033[0m...')
    sleep(1)
    if a > b:
        c *= -1
        b -= 1
    if a < b:
        b += 1
    cont = 0
    for c in range(a, b, c):
        print(f'\033[33m{c:^3}\033[0m', end=' ')
        cont += 1
        #sleep(0.5)
        if cont == 11:
            print()
            cont = 0
    print()
    print('~'*30)


contador(1, 10, 1)
contador(10, 0, -2)
print('Faça a sua contagem personalizada!')
i = int(input('Começando em:  '))
f = int(input('Terminando em: '))
p = int(input('Com passo de:  '))
contador(i, f, p)