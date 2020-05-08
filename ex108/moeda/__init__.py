def metade(n):
    m = n/2
    return m


def dobro(n):
    d = n*2
    return d


def aumentar(n, p):
    m = n + (n*p/100)
    return m


def diminuir(n, p):
    d = n - (n*p/100)
    return d


def moeda(n):
    return f'R${n:.2f}'
