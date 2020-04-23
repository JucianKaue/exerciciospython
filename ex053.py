frase = str(input('Escreva uma frase: ').upper().strip())
palavras = frase.split()
junta = ''.join(palavras)
'''inverso = ''
for letra in range(len(junta) -1, -1, -1):
    inverso += junta[letra]'''
#ou
inverso = junta[::-1]
print('A frase {} invertida fica {}'.format(junta, inverso))
if junta == inverso:
    print('A frase é um palíndromo')
else:
    print('A frase não é um palíndromo')
