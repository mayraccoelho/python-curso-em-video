print('=' * 40)
txt = 'Desafio 035 - Analisando Triângulo v1.0'
print('\33[1:30:41m{:^40}\33[m'.format(txt))
print('=' * 40)

'''Desenvolva um programa que leia o comprimento de três retas e diga ao 
usuário se elas podem ou não formar um triângulo.'''

l1 = float(input('LADO 1: '))
l2 = float(input('LADO 2: '))
l3 = float(input('LADO 3: '))

if l1 + l2 > l3 and l2 + l3 > l1 and l3 + l1 > l2:
    print('Forma um triângulo!')
else:
    print('Não forma um triângulo!')
