print('=' * 40)
txt = 'Desafio 048 - Soma ímpares múltiplos de três'
print('\33[1:30:41m{:^40}\33[m'.format(txt))
print('=' * 40)

'''Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que
se encontram no intervalo de 1 até 500.'''

soma = 0
contador = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        contador += 1
        soma += i
print('A soma dos {} números ímpares e múltiplos de 3: {}' .format(contador, soma))