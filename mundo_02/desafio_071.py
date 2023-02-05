import random

print('=' * 40)
txt = 'Desafio 071 - Simulador de Caixa Eletrônico'
print('\33[1:30:41m{:^40}\33[m'.format(txt))
print('=' * 40)

''' Crie um programa que simule o funcionamento de um caixa eletrônico.
No início, pergunte ao usuário qual será o valor a ser sacado (inteiro)
e o programa vai informar quantas cédulas de cada valor serão entregues.
Obs.: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1. '''

print('==== CAIXA ELETRÔNICO ====')
valor = int(input('Valor de Saque: ')) # 90
total = valor # 90
cedula = 50
cont = 0

while True:
    if total >= cedula: # Se 90 for maior ou igual a 50
        total -= cedula # total recebe - cedula. total agora vale 40
        cont += 1 # cont 1
    else:
        if cont > 0:
            print(f'Total de {cont} cédulas de R${cedula:.2f}') # total de 1 cedula de 50 reais
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        cont = 0
        if total == 0:
            break
