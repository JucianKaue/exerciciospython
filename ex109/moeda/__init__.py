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
