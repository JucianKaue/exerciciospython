def fatorial(n, show=False):
    """
-->> Mostra o fatorial de um número
    parametro n: número pra o qual será mostrado o fatorial
    parametro show: (opcional) define se o processo de cálculo será mostrado
    return: Fatorial de n
    """
    from time import sleep
    f = n
    for c in range(n, 0, -1):
        if show:
            if c != n:
                f *= c
            if c == 1:
                print(f'{c}', end=' = ')
            else:
                print(f'{c}', end=' x ')
            sleep(0.5)
        else:
            f *= c
    return f


# Programa Principal
print(f'{fatorial(5, show=True)}')
help(fatorial)
