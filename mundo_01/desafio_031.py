print('=' * 40)
txt = 'Desafio 030 - Custo da Viagem'
print('\33[1:30:41m{:^40}\33[m'.format(txt))
print('=' * 40)

'''Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem,
cobrando R$0,50 por Km para viagens até 200Km e R$0,45 para viagens mais longas.'''

distancia = int(input('Para calcular o preço da passagem preciso saber qual é a distância a ser percorrida: '))
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45

print('Você vai viajar {}Km.\nValor da viagem: R${:.2f}' .format(distancia, preco))
