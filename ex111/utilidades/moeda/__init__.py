def dobro(n, moeda=False):
    d = n * 2
    if moeda:
        return f'R${d:.2f}'
    else:
        return d


def metade(n, moeda=False):
    m = n / 2
    if moeda:
        return f'R${m:.2f}'
    else:
        return m


def aumentar(n, p, moeda=False):
    m = n + (n*p/100)
    if moeda:
        return f'R${m:.2f}'
    else:
        return m


def diminuir(n, p, moeda=False):
    d = n - (n*p/100)
    if moeda:
        return f'R${d:.2f}'
    else:
        return d


def format(n):
    return f'R${n:.2f}'


def resumo(n, d, a):
    from ex111.utilidades import dados
    print('¬'*30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('¬'*30)
    print(f'{"Preço analizado:":<20}{format(n)}')
    print(f'{"Dobro do Preço:":<20}{dobro(n, True)}')
    print(f'{"Metade do preço:":<20}{metade(n, True)}')
    print(f'{f"Diminuindo {d}%:":<20}{diminuir(n, d, True)}')
    print(f'{f"Aumentando {a}%:":<20}{aumentar(n, d, True)}')
    print('¬'*30)
