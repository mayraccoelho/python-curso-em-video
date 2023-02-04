print('=' * 40)
txt = 'Desafio 014 - Conversor de Temperaturas'
print('\33[1:30:41m{:^40}\33[m'.format(txt))
print('=' * 40)

'''Escreva um programa que converta uma temperatura digitada em °C e converta para °F.'''

celcius = int(input('TEMPERATURA EM °C: '))

print('°C: {}\n°F: {}' .format(celcius, celcius * 1.8 + 32))