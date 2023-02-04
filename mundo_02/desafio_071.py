import random

print('=' * 40)
txt = 'Desafio 071 - Simulador de Caixa Eletrônico'
print('\33[1:30:41m{:^40}\33[m'.format(txt))
print('=' * 40)

''' Crie um programa que simule o funcionamento de um caixa eletrônico.
No início, pergunte ao usuário qual será o valor a ser sacado (inteiro)
e o programa vai informar quantas cédulas de cada valor serão entregues.
Obs.: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1. '''

somaValores = cont1 = cont10 = cont20 = cont50 = 0

while True:
    print('==== CAIXA ELETRÔNICO ====')

    valor = int(input('Valor de Saque: '))
    cedulas = [1, 10, 20, 50]
    cedulas = random.choice(cedulas)

    if cedulas == 1:
        cont1 += 1
    if cedulas == 10:
        cont1 += 1
    if cedulas == 20:
        cont1 += 1
    if cedulas == 50:
        cont1 += 1

