valorcasa = float(input('Valor da casa: R$'))
salario = float(input('Qual é o seu salario? R$'))
anos = int(input('Em quantos anos você vai pagar? '))
prestacao = valorcasa/(anos*12)
if (salario/100*30) >= prestacao:
    print('Seu empréstimo no valor de R${:.2f}, com prestação de R${:.2f} foi \033[1;32maceito'.format(valorcasa,prestacao))
elif (salario/100*30) <= prestacao:
    print('Seu empréstimo no valor de R${:.2f}, com prestação de R${:.2f} foi \033[1;31mnegado'.format(valorcasa,prestacao))
