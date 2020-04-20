n = float(input('Digite um valor em metros: '))
km = n / 1000
hec = n / 100
decã = n / 10
c = n * 100
m = n * 1000
deci = n *10
print('O valor {}m é igual a: \n{}Kilometros\n{}Hectometros\n{}Decãmetros\n{}Decimetros\n{}centimetros\n{}milímetros'.format(n,km,hec,decã, deci, c, m))
