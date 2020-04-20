v = int(input('Escreva a velocidade do carro em Km/h: '))
if v <= 80:
    print('Você não foi multado')
else:
    m = (v-80)*7
    print('Você foi multado em R$ {:.2f}'.format(m))
