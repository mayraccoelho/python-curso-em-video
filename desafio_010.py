print('=' * 40)
txt = 'Desafio 010 - Conversor de Moedas'
print('\33[1:30:41m{:^40}\33[m'.format(txt))
print('=' * 40)

'''Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. Considere U$$1,00 = R$3,27'''

real = float(input('Quanto você tem de dinheiro? R$ '))
dolar = real / 3.27

print('Com R${:.2f} você pode comprar U$${:.2f}' .format(real, dolar))