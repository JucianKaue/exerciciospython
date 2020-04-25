numeros = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze',
           'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    while True:
        numero = int(input('Escreva um número de 1 a 20: '))
        if 0 <= numero <= 20:
            break
        print('Verifique os dados')
    print(f'O número \033[32m{numero}\033[0m por extenso é \033[32m{numeros[numero]}\033[0m')
    opcao = input('Quer continuar? [S/N] ').strip().lower()
    if opcao == 'n':
        break
