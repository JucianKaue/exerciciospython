km = float(input('quantos kilometros rodados? '))
d = float(input('quantos dias alugado? '))
p = (60*d)+(0.15*km)
print('O total a pagar é R${:.2f}'.format(p))
