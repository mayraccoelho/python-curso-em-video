print('=' * 40)
txt = 'Desafio 038 - Comparando Números'
print('\33[1:30:41m{:^40}\33[m'.format(txt))
print('=' * 40)

'''Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais'''


while True:
    try:
        numero1 = int(input('Número 1: '))
        numero2 = int(input('Número 2: '))

        if numero1 > numero2:
            print('O número {} é maior!' .format(numero1))
            break
        elif numero2 > numero1:
            print('O número {} é maior!' .format(numero2))
            break
        else:
            print('Os números são iguais!')
            break
    except ValueError:
        print('Por favor digite um número!')