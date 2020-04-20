import math
b = float(input('Comprimento do cateto oposto: '))
c = float(input('Comprimento do cateto adjacente: '))
#a = math.sqrt(b**2 + c**2)
#ou
a = math.hypot(b, c)
print('O comprimento da hipotenusa é {:.2f}'.format(a))