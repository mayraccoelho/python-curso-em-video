print('=' * 40)
txt = 'Desafio 052 - Números Primos'
print('\33[1:30:41m{:^40}\33[m'.format(txt))
print('=' * 40)

'''Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.'''

n = int(input('Digite um número: '))
total = 0
for i in range (1, n + 1):
    if n % i == 0:
        print('\33[34m', end='')
        total += 1
    else:
        print('\33[31m', end='')
    print('{} ' .format(i), end='')
print('\n\33[mO número {} foi divisível {} vezes.' .format(n, total), end='\n')
if total == 2:
    print('Por isso ele é PRIMO!')
else:
    print('Por isso ele não é PRIMO!')

''' ERRADO if n % 1 == 0 and n % n == 0:
        print('{} NÚMERO PRIMO')
    else:
        print('NÚMERO NÃO É PRIMO')'''