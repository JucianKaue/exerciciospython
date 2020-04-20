n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
m = (n1+n2)/2
if 0 <= m < 5.0:
    print('A media foi de {:.1f}\nSituação do aluno: \033[1;31m REPROVADO'.format(m))
elif 5.0 <= m <= 6.9:
    print('A média do aluno foi de {:.1f}\nSituação do auno: \033[1;33m RECUPERAÇÃO'.format(m))
elif 7.0 <= m <= 10:
    print('A média do aluno foi de {:.1f}\nSituação do aluno: \033[1;32m APROVADO'.format(m))
else:
    print('\033[1;30;41mERRO\033[0m\nAs notas precisam ser entre 0 e 10, confira os valores inseridos')