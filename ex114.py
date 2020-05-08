import requests

try:
    pudim = requests.head(url='http://pudim.com.br/')
except:
    print('\033[33mO pudim não está acessivel momento :(\033[0m')
else:
    print('\033[32mO pudim ta on\033[0m')
