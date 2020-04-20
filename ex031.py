km = int(input('Digite a distância de sua viagem em Km: '))
print('Você está começando uma viagem de {}Km.')
# preço = distância *  if distância <= 200 else distância * if km <= 200 * 0.45
   #  maneira simplificada do if
if km <= 200:
    print('O preço da sua passagem é R${:.2f} '.format(km*0.50))
else:
    print('O preço da sua passagem é R${:.2f}'.format(km*0.45))
