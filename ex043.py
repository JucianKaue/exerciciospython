print('\033[1;31m+-'*20)
print('\033[1;32mCALCULADORA DE ÍNDICE DE MASSA CORPORAL')
print('\033[1;31m+-'*20)
peso = float(input('\033[0mQual é o seu peso? '))
altura = float(input('Qual é a sua altura em centimetros? '))
imc = peso/((altura/100)**2)
if imc < 18.5:
    print('Seu índice de massa corporal é de {:.2f}\nSeu estado: \033[1;33mAbaixo do Peso.'.format(imc))
elif imc <= 25:
    print('Seu indice de massa corporal é de {:.2f}\nSeu estado: \033[1;32mPeso ideal.'.format(imc))
elif imc <= 30:
    print('Seu indice de massa corporal é de {:.2f}\nSeu estado: \033[1;33mSobrepeso.'.format(imc))
elif imc <= 40:
    print('Seu indice de massa corporal é de {:.2f}\nSeu estado: \033[1;33mObesidade'.format(imc))
elif imc > 40:
    print('Seu índice de massa corporal é de {:.2f}\nSeu estado: \033[1;31mObesidade Mórbida'.format(imc))
