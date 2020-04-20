import datetime
ano = int(input('Ano de nascimento: '))
idade = datetime.date.today().year - ano
if idade < 18:
    print('Você vai precisar se alistar ao serviço militar daqui a {} anos'.format(18-idade))
elif idade == 18:
    print('Está na hora de se alistar.\n\033[1;47mBoa sorte soldado\033[0m')
else:
    print('Você já deveria ter se alistado a {} anos.'.format(idade-18))
