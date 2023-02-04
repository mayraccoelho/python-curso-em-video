print('=' * 40)
txt = 'Desafio 006 - Dobro, Triplo e Raiz'
print('\33[1:30:41m{:^40}\33[m'.format(txt))
print('=' * 40)

'''Crie um algoritimo que leia um número e mostre o seu dobro, triplo e raiz quadrada.'''
import math

numero = int(input('Digite um número: '))
dobro = numero * 2
triplo = numero * 3
raiz = math.sqrt(numero) # Ou: numero ** (1/2) Ou: pow(numero, 1/2)

print('O dobro de {} é: {}.\nO triplo de {} é: {}.\nA raiz quadrada de {} é: {:.2f}.' .format(numero, dobro, numero, triplo, numero, raiz))