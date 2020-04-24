s = count = 0
while True:
    n = float(input('Escreva um número [999 para parar]: '))
    if n == 999:
        break
    s += n
    count += 1
if s == int(s):
    print(f'A soma entre os {count} digitados é {s:.0f}')
else:
    print(f'A soma dos {count} numeros digitados é {s}')
