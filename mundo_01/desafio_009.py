print('=' * 40)
txt = 'Desafio 009 - Tabuada'
print('\33[1:30:41m{:^40}\33[m'.format(txt))
print('=' * 40)

'''Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.'''

numero = int(input('Digite um número para ver a tabuada: '))

print('.' * 12)
for i in range(0,11):
    print('{} x {:2} = {}' .format(numero, i, numero * i))
print('.' * 12)

