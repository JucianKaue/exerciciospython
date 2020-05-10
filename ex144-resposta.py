import urllib.request

try:
    urllib.request.urlopen('http://pudim.com.br')
except:
    print('\033[31mO pudim ta off :(')
else:
    print('\033[31mO pudim ta off :(')
