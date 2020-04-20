h = float(input('Escreva a altura da parede em metros: '))
l = float(input('Escreva a largura da parede em metros: '))
a = h*l
t = a/2
print('A quantidade de tinta necessária pra pintar a parede de dimensões {}x{}, ou seja, {} m² é {} litros de tinta'.format(h, l, a, t))
