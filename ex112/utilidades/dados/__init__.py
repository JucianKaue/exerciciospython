def leiaDinheiro(msg):
    n = input(msg).strip() #.replace(',', '.')
    while not n.isnumeric():
        if ',' in n:
            l = []
            for e in n:
                l.append(e)
            l.insert(l.index(','), '.')
            l.remove(',')
            n = ''.join(l)
            return float(n)
        else:
            print(f'\033[31mERRO, "{n}" não é um valor válido\033[0m')
            n = input(msg)
    return float(n)
