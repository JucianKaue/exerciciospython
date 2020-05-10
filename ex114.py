import requests

print('='*5, '\033[33mVERIFICANDO A SITUAÇÃO DO PUDIM\033[0m', '='*5)
try:
    requests.head(url='http://pudim.com.br/')
except:
    print('\033[31mO pudim ta off :(\033[0m')
else:
    print('\033[32mO pudim ta on :)\033[0m')
