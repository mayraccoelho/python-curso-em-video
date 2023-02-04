from time import sleep

print('=' * 40)
txt = 'Desafio 046 - Contagem Regressiva'
print('\33[1:30:41m{:^40}\33[m'.format(txt))
print('=' * 40)

'''Faça um programa que mostra na tela uma contagem regressiva para o estouro de fogos de artifício, 
indo de 10 até 0, com uma pausa de 1 segundo entre eles.'''
print('=-'*20)
print('\33[1:42m{:^40}\33[m'.format('CONTAGEM REGRESSIVA'))
print('=-'*20)

for c in range(10, 0, -1):
    sleep(1)
    print(c)
sleep(1)
print('=-'*20)
print('\33[1:42m{:^40}\33[m'.format('FELIZ ANO NOVO \o/'))
print('=-'*20)