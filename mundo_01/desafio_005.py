print('=' * 40)
txt = 'Desafio 005 - Antecessor e Sucessor'
print('\33[1:30:41m{:^40}\33[m'.format(txt))
print('=' * 40)

'''Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.'''

numero = int(input('Digite um número: '))
antecessor = numero - 1
sucessor = numero + 1
print('O antecessor de {} é: {}.\nO sucessor de {} é: {}.' .format(numero, numero - 1, numero, numero + 1))