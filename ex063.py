count = 0
s = 0
n1 = 0
n2 = 1
elementos = 0
print('-'*7, 'SEQUENCIA DE FIBONACCI', '-'*7)
while elementos == 0:
    elementos = int(input('Quantidade de elementos da sequência: '))
if elementos == 1:
    print("0")
while not count == elementos - 1:
    count += 1
    s = n1 + n2
    n2 = n1
    n1 = s
    if count == 1:
        print('0 -> ', end='')
    if count == elementos - 1:
        print(s)
    else:
        print(s, end=' -> ')
