def area(c, l):
    area = c*l
    print(f'A área do terreno \033[33m{c}x{l}\033[0m é \033[32m{area:.2f}m²\033[0m')


print('-'*30)
print(f'{"ANALIZADOR DE TERENOS":^30}')
print('-'*30)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(c, l)
