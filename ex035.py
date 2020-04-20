print('/=='*20)
print('Analizador de triângulos')
print('/=='*20)
c1 = float(input('Comprimento da primeira reta: '))
c2 = float(input('Comprimento da segunda reta: '))
c3 = float(input('Comprimento da terceira reta: ' ))
if c1 < c2 + c3 and c2 < c3 + c1 and c3 < c1 + c2:
    print('Esses segmentos podem formar triângulos')
else:
    print('Esses segmentos podem formar triângulos')
'''if c3>c1 or c2:
    if c3<c2+c1:
        print('Essas retas podem formar um triângulo.')
    else:
        print('Essas retas não podem formar um triângulo.')
elif c2>c1 or c3:
    if c2 < c1 + c3:
        print('Essas retas podem formar um triângulo.')
    else:
        print('Essas retas não podem formar um triângulo.')
elif c1>c2 or c3:
    if c1<c2+c3:
        print('Essas retas podem formar um triângulo.')
    else:
        print('Essas retas não podem formar um triângulo.')'''
