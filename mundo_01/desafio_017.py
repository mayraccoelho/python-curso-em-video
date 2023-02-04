print('=' * 40)
txt = 'Desafio 017 - Catetos e Hipotenusa'
print('\33[1:30:41m{:^40}\33[m'.format(txt))
print('=' * 40)

'''Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente 
de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.'''

import math
co = float(input('CATETO OPOSTO: '))
ca = float(input('CATETO ADJACENTE: '))
hi = math.hypot(co,ca) # ou co ** 2 + ca ** 2 ** (1/2)
print('HIPOTENUSA: {:.2f}' .format(hi))