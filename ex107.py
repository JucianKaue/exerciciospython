from ex107 import moeda

p = float(input('Digite o preço: R$ '))
print(f'A metade de R${p:.2f} é {moeda.metade(p)}')
print(f'O dobro de R${p:.2f} é {moeda.dobro(p)}')
print(f'Aumentando 10% do valor, temos {moeda.aumentar(p, 10)}')
print(f'Diminuindo 10% do valor temos {moeda.diminuir(p, 10)}')
