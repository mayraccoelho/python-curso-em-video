print('=' * 40)
txt = 'Desafio 050 - Soma dos pares'
print('\33[1:30:41m{:^40}\33[m'.format(txt))
print('=' * 40)

'''Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
Se o valor for ímpar, desconsidere-o.'''
soma = 0
contador = 0
for i in range(1,7):
    n = int(input('Digite número {}: ' .format(i)))
    if n % 2 == 0:
        soma += n
        contador += 1
print('Você informou {} números pares e a soma deles é {}'.format(contador, soma))