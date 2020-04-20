import random
a1 = str(input('Nome do primeiro aluno: '))
a2 = str(input('Nome do segundo aluno: '))
a3 = str(input('Nome do terceiro aluno: '))
a4 = str(input('Nome do quarto aluno: '))
names = [a1,a2,a3,a4]
print('O aluno que irá apagar o quadro é {}'.format(random.choice(names)))
