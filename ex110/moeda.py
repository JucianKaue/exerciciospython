def format(n):
    return f'R${n:.2f}'


def resumo(n, d, a):
    print('¬'*30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('¬'*30)
    print(f'{"Preço analizado:"} \t{format(n)}')
    print(f'{"Dobro do Preço:"} \t{format((n*2))}')
    print(f'{"Metade do preço:"} \t{format((n/2))}')
    print(f'{f"Diminuindo {d}%:"} \t{format((n-(n*a/100)))}')
    print(f'{f"Aumentando {a}%:"} \t{format((n+(n*a/100)))}')
    print('¬'*30)
