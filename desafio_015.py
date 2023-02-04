print('=' * 40)
txt = 'Desafio 015 - Aluguel de Carros'
print('\33[1:30:41m{:^40}\33[m'.format(txt))
print('=' * 40)

'''Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
e a quantidade de dias pelos quais ele foi alugado. 
Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.'''

km = float(input('Km percorridos: '))
dias = int(input('Dias: '))
preco = (dias * 60) + (km * 0.15)

print('PERCURSO: {:.0f} Km/h\nQUANTIDADE DE DIAS: {}\nPREÇO: R${:.2f}' .format(km, dias, preco))