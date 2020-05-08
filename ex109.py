from ex109 import moeda

p = float(input('Digite o preço: '))
print(f'O dobro de {moeda.format(p)} é {moeda.dobro(p, moeda=True)}')
print(f'A metade de {moeda.format(p)} é {moeda.metade(p, moeda=True)}')
print(f'Aumentando 20% de {moeda.format(p)}, temos {moeda.aumentar(p, 20, moeda=True)}')
print(f'Diminuindo 20% de {moeda.format(p)}, temos {moeda.diminuir(p, 20, moeda=True)}')
