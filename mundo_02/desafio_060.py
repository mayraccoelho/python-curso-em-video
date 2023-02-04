print('=' * 40)
txt = 'Desafio 060 - Cálculo do Fatorial'
print('\33[1:30:41m{:^40}\33[m'.format(txt))
print('=' * 40)

'''Faça um programa que leia um número qualquer e mostre o seu fatorial.
Ex: 5! = 5x4x3x2x1=120'''

n = int(input('Número: '))
fatorial = 1
count = n
print('{}! = '.format(n), end='')
while n > 0:
    print('{}' .format(count), end='')
    print(' x ' if count > 1 else ' = ', end='')
    count -= 1
    fatorial *= n
    n -= 1
print('{}'.format(fatorial), end='')
