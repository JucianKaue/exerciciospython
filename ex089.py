alunos = []
aluno = []
notas = []
while True:
     aluno.append(input('Nome do aluno: '))
     notas.append(float(input('Primeira nota: ')))
     notas.append(float(input('Segunda nota: ')))
     aluno.append(notas[:])
     alunos.append(aluno[:])
     aluno.clear()
     notas.clear()
     while True:
         r = input('Quer continuar? [S/N] ').strip().title()[0]
         if r in 'SN':
             break
     if r == 'N':
         break
print('=' * 10, 'BOLETIM', '=' * 10)
print(f'\033[32mNº    NOME        MÉDIA\033[0m')
for c in range(len(alunos)):
    print(f'{c:<6}', end='')
    print(f'{alunos[c][0].title():13}', end='')
    print(f'{((alunos[c][1][0]+alunos[c][1][1])/2):.1f}', end='')
    print()
print('-'*29)
while True:
    a = int(input('Você deseja saber as notas de qual aluno?  [999 para fechar]: '))
    if a == 999:
        break
    if a <= len(alunos):
        print(f'As notas do aluno(a) \033[32m{alunos[a][0].title()}\033[0m são: \033[32m{alunos[a][1][0]}\033[0m e \033[32m{alunos[a][1][1]}\033[0m')
