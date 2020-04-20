s = float(input('Qual é o salario do seu funcionário? R$'))
if s>1250.00:
   print('O valor de seu aumento é {:2f}, portanto o seu novo salario é de R${:.2f}'.format(s/100*10,s+(s / 100 * 10) ))
else:
    print('O valor de seu aumento é {:.2f}, portanto o seu novo salario é de R${:.2f}'.format(s/100*15,s+(s/100*15)))
