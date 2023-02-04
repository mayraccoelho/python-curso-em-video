from datetime import date

print('=' * 40)
txt = 'Desafio 032 - Ano Bissexto'
print('\33[1:30:41m{:^40}\33[m'.format(txt))
print('=' * 40)

'''Faça um programa que leia um ano qualquer e mostre se é BISSEXTO.'''

ano = int(input('Escolha um ano. Para selecionar ano atual é só digitar 0: '))
if ano == 0:
    ano = date.today().year
    print('O ano atual é {}.' .format(ano))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('Ano {} é Bissexto' .format(ano))
else:
    print('Ano {} não é Bissexto!' .format(ano))