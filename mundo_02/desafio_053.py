print('=' * 40)
txt = 'Desafio 053 - Detector de Palíndromo'
print('\33[1:30:41m{:^40}\33[m'.format(txt))
print('=' * 40)

'''Crie um programa que leia uma frase qualquer e diga se ela é um palindromo, desconsiderando os espaços.'''

frase = input('Digite uma frase... ').replace(' ', '')
fraseContrario = frase[::-1]

print('O inverso de {} é {}' .format(frase, fraseContrario))
if frase == fraseContrario:
    print('\33[33mE é um PALÍNDROMO!\33[m')
else:
    print('\33[31mE não é palíndromo!\33[m')