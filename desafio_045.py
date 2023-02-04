import random
from time import sleep
# CURSO EM VIDEO https://www.youtube.com/watch?v=tapTa6KVG-A

print('=' * 40)
txt = 'Desafio 045 - GAME: Pedra Papel e Tesoura'
print('\33[1:30:41m{:^40}\33[m'.format(txt))
print('=' * 40)

'''Crie um programa que faça o computador jogar jokenpô com você.'''
itens = ["PEDRA", "PAPEL", "TESOURA"]
computador = random.choice(itens)

usuario = input("""[1] PEDRA
[2] PAPEL
[3] TESOURA
Qual é a sua jogada? """)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!!!!!')
sleep(2)

ganhaPedra = usuario == '1' and computador == 'TESOURA'
ganhaPapel = usuario == '2' and computador == 'PEDRA'
ganhaTesoura = usuario == '3' and computador == 'PAPEL'
empatePedra = usuario == '1' and computador == 'PEDRA'
empatePapel = usuario == '2' and computador == 'PAPEL'
empateTesoura = usuario == '3' and computador == 'TESOURA'

print('=-' * 20)
print('Computador jogou', computador)
print('Você jogou ', end='')
if usuario == '1': print('PEDRA')
elif usuario == '2': print('PAPEL')
elif usuario == '3': print('TESOURA')
print('=-' * 20)

if ganhaPedra or ganhaPapel or ganhaTesoura:
    print('VOCÊ GANHOU!')
elif empatePedra or empatePapel or empateTesoura:
    print('DEU EMPATE!')
else:
    print('VOCÊ PERDEU!')