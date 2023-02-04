print('=' * 40)
txt = 'Desafio 016 - Quebrando um número'
print('\33[1:30:41m{:^40}\33[m'.format(txt))
print('=' * 40)

'''Crie um programa que leia um número Real qualquer pelo teclado e mostre
na tela a sua porção inteira. 
Ex: Digite um número: 6.127
O número 6.127 tem a parte inteira 6.'''

from math import trunc
numero = float(input('NÚMERO INTEIRO: '))
print('PORÇÃO INTEIRA É: {}' .format(trunc(numero)))
## OU
numero = float(input('NÚMERO INTEIRO: '))
print('PORÇÃO INTEIRA É: {}' .format(int(numero)))