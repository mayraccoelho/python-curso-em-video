print('=' * 40)
txt = 'Desafio 061 - Progressão Aritmética v2.0'
print('\33[1:30:41m{:^40}\33[m'.format(txt))
print('=' * 40)

'''Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos
da progressão usando a estrutura while.'''

primeiroTermo = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))
cont = 1

while cont <= 10:
    if cont < 10:
        print('{} --> ' .format(primeiroTermo), end='')
    elif cont == 10:
        print('{}' .format(primeiroTermo), end='')
    primeiroTermo += razao
    cont += 1

