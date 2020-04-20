from random import sample
n1 = str(input('Nome do primeiro aluno: '))
n2 = str(input('Nome do segundo aluno: '))
n3 = str(input('Nome do terceiro aluno: '))
n4 = str(input('Nome do quarto aluno: '))
l = [n1, n2, n3, n4]
print('A ordem de apresentação de trabalhos será: \n{}'.format(sample(l, 4)))
