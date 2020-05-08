def voto(nasc):
    from datetime import datetime
    idade = datetime.today().year - nasc
    if idade < 16:
        return f'Com {idade} anos. Você tem \033[31mVOTO NEGADO\033[0m'
    elif idade < 18 or idade > 65:
        return f'Com {idade} anos. Você tem \033[33mVOTO OPCIONAL\033[0m'
    elif idade < 65:
        return f'Com {idade} anos. Você tem \033[32mVOTO OBRIGATÓRIO\033[0m'


#Programa Principal
print('¬'*40)
print(voto(int(input('Escreva seu ano de nascimento: '))))
print('¬'*40)
