print('=' * 40)
txt = 'Desafio 062 - Progressão Aritmética v2.0'
print('\33[1:30:41m{:^40}\33[m'.format(txt))
print('=' * 40)

'''Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando
ele disser que quer mostrar 0 termos.'''

primeiroTermo = int(input('PRIMEIRO TERMO: '))
razao = int(input('RAZÃO: '))
termo = primeiroTermo
total = 0
cont = 1
mais = 10

while mais != 0:
    total += mais
    while cont <= total:
        print('{} -> ' .format(termo), end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos.' .format(total))