print('=' * 40)
txt = 'Desafio 012 - Calculando Descontos'
print('\33[1:30:41m{:^40}\33[m'.format(txt))
print('=' * 40)

'''Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.'''

valor = float(input('VALOR: R$ '))

print('VALOR: {:.2f}\nVALOR COM DESCONTO: {:.2f}' .format(valor, valor - (valor * 5 / 100)))
