print('\033[1;31m//--'*6)
print('\033[1;32mAnalizador de Triângulos')
print('\033[31m//--'*6)
r1 = float(input('\033[0m\033[1mComprimento da primeira reta: '))
r2 = float(input('Comprimento da segunda reta: '))
r3 = float(input('Comprimento da terceira reta: \033[0m'))
if r1<r2+r3 and r2<r1+r3 and r3<r1+r2:
    print('\033[1;34mEstas retas podem formar um triângulo\033[0m')
    if r1==r2==r3:
        print('\033[32mEste triângulo tem todos os lados iguais\nPortanto é um triângulo \033[1mEquilátero')
    elif r1==r2!=r3 or r2==r3!=r1 or r1==r3!=r2:
        print('\033[32mEste triângulo tem 2 lados iguais\nPortanto é um triângulo \033[1mIsósceles')
    elif r1 != r2 != r3 != r1:
        print('\033[32mEste triângulo não tem nenhum lado igual\nPortanto é um triângulo \033[1mEscaleno')
else:
    print('\033[1;31mEstas retas não podem formar um triângulo\033[0m')
