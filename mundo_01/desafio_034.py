print('=' * 40)
txt = 'Desafio 034 - Aumentos múltiplos'
print('\33[1:30:41m{:^40}\33[m'.format(txt))
print('=' * 40)

'''Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1250,00, calcule um aumento de 10%.
Para inferiores ou iguais, o aumento é de 15%.'''

salario = float(input('Digite o seu salário: '))
print (salario)
if salario >= 1250.00:
    novo = salario + (salario * 10 / 100)
else:
    novo = salario + (salario * 15 / 100)

print('SALÁRIO ATUAL: R${:.2f}\nSALÁRIO COM AUMENTO: R${:.2f}' .format(salario, novo))