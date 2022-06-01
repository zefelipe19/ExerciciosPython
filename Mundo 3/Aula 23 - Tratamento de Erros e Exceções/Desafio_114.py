'''Exercício Python 114: Crie um código em Python que teste se o site pudim está acessível pelo computador usado.'''
import urllib
from urllib import request

try:
    site = urllib.request.urlopen("http://pudim.com.br")
except:
    print("Não consegui acessar o site pudim")
else:
    print("Consegui acessar o site pudim")
