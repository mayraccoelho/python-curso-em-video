from random import randint
from time import sleep

print('=' * 40)
txt = 'Desafio 058 - Jogo de Adivinhação v2.0'
print('\33[1:30:41m{:^40}\33[m'.format(txt))
print('=' * 40)

'''Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número de 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.'''
numero_sorteado = randint(0,10)
print('=-' * 20)
numero_usuario = int(input('Vou pensar em um número entre 0 e 10. Tente adivinhar...\nEm que número eu pensei? '))
contadorTentativas = 1
print('=-' * 20)

print("\33[1:30:43mPROCESSANDO.... \33[m")
sleep(2)
while numero_usuario != numero_sorteado:
    if numero_usuario > numero_sorteado:
        print('\33[0:31mHuuum.. Você ERROU...\33[m\nO meu número é menor... ')
    else:
        print('\33[0:31mHuuum.. Você ERROU...\33[m\nO meu número é maior... ')
    numero_usuario = int(input('Tente novamente: '))
    print("\33[1:30:43mPROCESSANDO.... \33[m")
    sleep(2)
    contadorTentativas += 1

print('\n\33[0:30:46m===== Parabéns!! Você acertou! Eu pensei no número {} =====\33[m\nVocê precisou de \33[1:30:43m{} tentativas\33[m para acertar!' .format(numero_sorteado, contadorTentativas))