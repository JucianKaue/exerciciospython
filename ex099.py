def maior(* num):
    if len(num) == 0:
        print('Você não informou nenhum valor')
    else:
        from time import sleep
        cont = 0
        for v in num:
            cont += 1
            if cont == 1:
                m = v
            if v > m:
                m = v
        print('¬'*50)
        print(f'Os \033[33m{len(num)}\033[0m valores informados são ', end='')
        for v in num:
            print(f'\033[33m{v}\033[0m ', end='')
            sleep(0.5)
        print()
        print(f'O maior valor informado é \033[32m{m}\033[0m')
        print('¬'*50)


maior(8, 9, 3, 9, 6, 3)
maior()
maior(186, 5432, 453, 43, 65, 78, 43, 24, 6, 5, 7, 6, 786, 87, 676, 5, 875, 6765, 876, 675, 87, 85, 8, 6787, 6)