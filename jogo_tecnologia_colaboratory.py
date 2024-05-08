# -*- coding: utf-8 -*-
"""Olá, este é o Colaboratory

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/notebooks/intro.ipynb
"""

# trazendo a bliblioteca capaz de realizar requisiçoes
import requests
import random

# una variável chamada url que amazena o endereço com as info que desejo buscar
url = 'https://raw.githubusercontent.com/guilhermeonrails/api-imersao-ia/main/words.json'
# faço a requisição e armazeno em uma variável chamada resposta
resposta = requests.get(url)
# transforma a resposta em JSON
data = resposta.json()
# exibindo as informações com o comando print
print(data)

# variável chamada valor secreto que armazena uma tecnologia aleatoria da lista
valor_secreto = random.choice(data)
# variável para armazenar apenasss a palavra
palavra_secreta = valor_secreto['palavra']
# variável para armazenar apenas a dica
dica = valor_secreto['dica']
# mostrou na tela quantas letras a palavra secreta possui e a dica
# o f é capaz de juntar palavras e variáveis
# receber o chute ou palpite da tecnologia
print(f'A palavra secreta tem {len(palavra_secreta)} letras')
print(f'A dica é -> {dica}')
chute = input('O que você acha que é ')
if chute == palavra_secreta:
  print('Acertou')
else:
  print(f'Errou.. a palavra secreta era {palavra_secreta}')