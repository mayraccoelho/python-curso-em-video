print('=' * 40)
txt = 'Desafio 018 - Cosseno e Tangente'
print('\33[1:30:41m{:^40}\33[m'.format(txt))
print('=' * 40)

'''Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.'''

import math
a = float(input('ÂNGULO: '))
radiano = math.radians(a)
s = math.sin(radiano)
c = math.cos(radiano)
t = math.tan(radiano)

print('SENO: {:.2f}\nCOSSENO: {:.2f}\nTANGENTE: {:.2f}' .format(s, c, t))