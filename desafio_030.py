print('=' * 40)
txt = 'Desafio 030 - Par ou Ímpar'
print('\33[1:30:41m{:^40}\33[m'.format(txt))
print('=' * 40)

'''Escreva um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.'''

numero = int(input('Diga um número: '))
if numero % 2 == 0:
    print('O número {} é PAR' .format(numero))
else:
    print('O número {} é ÍMPAR' .format(numero))
