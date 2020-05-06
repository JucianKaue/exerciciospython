from random import randint
from time import sleep
from operator import itemgetter
jogador = {}
print('='*11, '\033[32mDADOS\033[0m', '='*11)
for j in range(1, 5):
    jogador[f'jogador{j}'] = randint(1, 6)
for k, v in jogador.items():
    sleep(0.5)
    print(f'O {k} tirou {v} nos dados')
ranking = sorted(jogador.items(), key=itemgetter(1), reverse=True)
print('='*14, '\033[32mRANKING\033[0m', '='*13)
sleep(0.5)
for c, v in enumerate(ranking):
    print(f'  -> {c+1}º lugar: {v[0]} com {v[1]} pontos')
    sleep(0.5)
