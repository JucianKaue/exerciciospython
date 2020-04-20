preco = float(input('Preço do produto: '))
pagamento = str(input('(Cartao, dinheiro ou cheque)\nCondição de pagamento: '))
p = pagamento.strip().lower().split()
if 'dinheiro' in p:
    print('O preço inicial é de R${:.2f} e o preço com desconto é de R${:.2f}'.format(preco,preco-(preco/100*10)))
elif 'cheque' in p:
    print('O preço inicial é de R${:.2f} e o preço com desconto é de R${:.2f}'.format(preco, preco - (preco / 100 * 10)))
elif 'cartao' in p:
    vezes = int(input('Quantas vezes? '))
    if vezes == 1:
        print('O preço inicial é de R${:.2f} e o preço com desconto é de R${:.2f}'.format(preco,preco-(preco/100*5)))
    elif vezes == 2:
        print('O preço é R${:.2f}'.format(preco))
    elif vezes > 2:
        print('O preço inicial é de R${:.2f} e o preço com juros é de R${:.2f}'.format(preco,preco+(preco/100*20)))
    else:
        print('\033[1;30;41mERRO\033[0m\nVerifique os dados inseridos e tente novamente')
else:
    print('\033[1;30;41mERRO\033[0m\nVerifique os dados inseridos e tente novamente')
