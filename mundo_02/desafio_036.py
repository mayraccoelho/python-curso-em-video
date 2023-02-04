print('=' * 40)
txt = 'Desafio 036 - Aprovando Empréstimo'
print('\33[1:30:41m{:^40}\33[m'.format(txt))
print('=' * 40)

'''Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.

Calcule o valor da prestação mensal sabendo que ela não pode exceder 30% do salário ou então 
o empréstimo será negado.'''


print('\33[1:30:42m{:^40}\33[m'.format('Simulação de Financiamento'))
casa = float(input('Valor do imóvel: R$ '))
salario = float(input('Salário do Comprador: R$ '))
anos = int(input('Quantos anos de financiamento?'))
prestacao = casa / (anos * 12)

if prestacao >= (salario * 30 / 100):
    print('\33[1:31m\nFINANCIAMENTO NEGADO\33[m\n'
          'Tempo de financiamento solicitado: {} anos\nPrestação: R${:.2f}'
          '\nO valor da prestação ultrapassa 30% do seu salario!' .format(anos, prestacao))
else:
    print('\33[1:32m\nParabéns, financiamento aceito!\33[m\nTempo de financiamento solicitado: {} anos\nPrestação: R${:.2f}' .format(anos, prestacao))

