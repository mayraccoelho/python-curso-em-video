print('=' * 40)
txt = 'Desafio 013 - Reajuste Salarial'
print('\33[1:30:41m{:^40}\33[m'.format(txt))
print('=' * 40)

'''Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.'''

salario = float(input('Digite o seu sálario: '))

print('SALÁRIO ATUAL: {:.2f}\nSALÁRIO COM AUMENTO: {:.2f}' .format(salario, salario + (salario * 15 / 100)))