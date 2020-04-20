from random import randrange
from time import sleep
n = int(input('Estou pensando em um numero entre 0 e 5! \nTente adivinhar qual é: '))
n2 = randrange(5)
print('Processando...')
sleep(2)
if n == n2:
    print('Parabéns, você acertou')
else:
    print('Que pena, você errou! O numero era {}, tente novamente'.format(n2))
