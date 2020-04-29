elementos = list()
pos_a = list()
pos_f = list()
print('='*10, '\033[32mANALIZADOR DE EXPRESSÕES MATEMÁTICAS\033[0m', '='*10)
expressao = input('Escreva uma expressão matemática: ')
for pos, e in enumerate(expressao):
    elementos.append(e)
    if e == '(':
        pos_a.append(pos)
    elif e == ')':
        pos_f.append(pos)
count = 0
if elementos.count('(') == elementos.count(')'):
    for c, pa in enumerate(pos_a):
        if pa < pos_f[c]:
            count += 1
    if count == len(pos_f):
        print('A expressão é \033[1;32mVÁLIDA\033[0m')
    else:
        print('A expressão é \033[1;31mINVÁLIDA\033[0m')
else:
    print('A expressão é \033[1;31mINVÁLIDA\033[0m')
