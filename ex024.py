cidade = str(input('Digite o nome de uma cidade: '))
#a = 'SANTO'in cidade.upper().split()[0]
#a = 'SANTO'in cidade.upper().strip()[:5]
a = cidade[:5].upper().strip() == 'SANTO'
print(a)
