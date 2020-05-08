def dobro(n, moeda=False):
    d = n * 2
    return d if moeda is False else format(d)


def metade(n, moeda=False):
    m = n / 2
    return m if moeda is False else format(n)


def aumentar(n, p, moeda=False):
    m = n + (n*p/100)
    return m if moeda is False else format(m)


def diminuir(n, p, moeda=False):
    d = n - (n*p/100)
    return d if moeda is False else format(d)


def format(n):
    return f'R${n:.2f}'.replace('.', ',')
