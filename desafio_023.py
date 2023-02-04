print('=' * 40)
txt = 'Desafio 023 - Separando dígitos de um número'
print('\33[1:30:41m{:^40}\33[m'.format(txt))
print('=' * 40)

'''Faça um programa que leia um número de 0 a 9999 e mostre na tela um dos dígitos separados.
Ex: 
Digite um número: 1834

Unidade: 4 Dezena: 3 Centena: 8 Milhar: 1'''

num = int(input('Digite um número de 0 a 9999: '))
n = str(num).zfill(4)

print('UNIDADE: {}' .format(n[3]))
print('DEZENA: {}' .format(n[2]))
print('CENTENA: {}' .format(n[1]))
print('MILHAR: {}' .format(n[0]))
