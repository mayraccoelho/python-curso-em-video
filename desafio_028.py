print('=' * 40)
txt = 'Desafio 028 - Jogo de Adivinhação v.1.0'
print('\33[1:30:41m{:^40}\33[m'.format(txt))
print('=' * 40)

'''Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.'''

from time import sleep
from random import randint

numero_sorteado = randint(1,5)
print('=-' * 20)
numero_usuario = int(input('Vou pensar em um número entre 1 e 5. Tente adivinhar...\nEm que número eu pensei? '))
print('=-' * 20)

print("\33[1:30:43mPROCESSANDO.... \33[m")
sleep(2)
print('\n\33[0:30:46m===== Parabéns!! Você acertou! Eu pensei no número {} =====\33[m' .format(numero_sorteado)) if (numero_sorteado == numero_usuario) else print('\n\33[0:30:41mPoxa, você errou! Eu pensei no número {} e não no {}!\33[m' .format(numero_sorteado,numero_usuario))