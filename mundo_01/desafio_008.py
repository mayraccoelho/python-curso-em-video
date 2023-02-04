print('=' * 40)
txt = 'Desafio 008 - Conversor de Medidas'
print('\33[1:30:41m{:^40}\33[m'.format(txt))
print('=' * 40)

'''Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.'''

metros = float(input('Distância em metros: '))
centimeros = metros * 100
milimetros = metros * 1000

print('{:.1f} metros corresponde a {:.0f} centímetros e a {:.0f} milímetros' .format(metros, centimeros, milimetros))