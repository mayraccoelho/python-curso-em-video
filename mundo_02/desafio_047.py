print('=' * 40)
txt = 'Desafio 047 - Contagem de Pares'
print('\33[1:30:41m{:^40}\33[m'.format(txt))
print('=' * 40)

'''Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.'''

for i in range(0, 51):
    if i % 2 == 0:
        virgula = ','
        if i == 50:
            virgula = virgula.replace(',', '')
        print(i, end=virgula)

#Outra forma que economiza no for, ele passa apenas uma vez no laço (algoritimo exige menos da maquina)
'''for i in range(2,51,2):
    virgula = ','
    if i == 50:
        virgula = virgula.replace(',', '')
    print(i, end=virgula)'''