import emoji
import datetime
print(emoji.emojize(':person_swimming:'*24))
print(emoji.emojize('\U0001F1E7\U0001F1F7   \033[1;32;43m CONFEDERAÇÃO BRASILEIRA DE NATAÇÃO\033[0m   \U0001F1E7\U0001F1F7'))
print(emoji.emojize(':person_swimming:'*24))
ano = int(input('\nEscreva o seu ano de nascimento para ver qual é sua categoria:\n'))
idade = datetime.date.today().year - ano
if 0 < idade <= 9:
    print('Você irá completar {} anos esse ano.\nCategoria: \033[1;36mMIRIM'.format(idade))
elif 0 < idade <= 14:
    print('Você irá completar {} anos esse ano.\nCategoria: \033[1;34mINFANTIL'.format(idade))
elif 0 < idade <=19:
    print('Você irá completar {} anos esse ano.\nCategoria: \033[1;33mJUNIOR'.format(idade))
elif 0 < idade == 20:
    print('Você irá completar {} anos esse ano.\nCategoria: \033[1;32mSÊNIOR'.format(idade))
elif idade <= 0:
    print('\033[1;41mERRO\033[0m\n\033[1mConfira o valor inserido')
else:
    print('Você irá completar {} anos esse ano.\nCategoria: \033[1;31mMASTER'.format(idade))
