print('=' * 40)
txt = 'Desafio 051 - Progressão Aritmética'
print('\33[1:30:41m{:^40}\33[m'.format(txt))
print('=' * 40)

'''Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.'''

primeiroTermo = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))
decimoTermo = primeiroTermo + (10 - 1) * razao
for i in range(primeiroTermo, decimoTermo + razao, razao):
    print('{} '.format(i), end='-> ')
print('ACABOU')