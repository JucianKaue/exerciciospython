count = total_gasto = caro = barato = 0
while True:
    count += 1
    print('-'*20)
    print('      MERCADIN')
    print('-'*20)
    produto = input('Nome do produto: ').strip().title()
    preco = float(input('Preço do produto: R$'))
    while True:
        opcao = input('Deseja continuar? (S/N) ').strip().upper()[0]
        if opcao in 'NS':
            break
    total_gasto += preco
    if preco > 1000:
        caro += 1
    if count == 1 or preco < barato_preco:
        barato_preco = preco
        barato = produto
    if opcao == 'N':
        break
print('_-'*15)
print(f'Total gasto: R${total_gasto:.2f}')
print(f'Quantidade de produtos que custam mais que R$1000: {caro}')
print(f'O produto mais barato é {barato}, que custa R${barato_preco:.2f}')
