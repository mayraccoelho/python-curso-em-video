print('=' * 40)
txt = 'Desafio 063 - Sequência de Fibonacci v1.0'
print('\33[1:30:41m{:^40}\33[m'.format(txt))
print('=' * 40)

'''Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma
Sequência de Fibonacci.
Ex: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8'''

n = int(input('Termo desejado: '))
a = 0
b = 1
cont = 2

while cont != n:
    if a == 0 and b == 1:
        print('{} -> {} -> ' .format(a, b), end='')
    f = a + b
    a = b
    b = f
    print('{} -> ' .format(f), end='')
    cont += 1
