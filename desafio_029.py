print('=' * 40)
txt = 'Desafio 029 - Radar Eletrônico'
print('\33[1:30:41m{:^40}\33[m'.format(txt))
print('=' * 40)

'''Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma
mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada Km acima do limite.'''

velocidade = int(input('Qual é a velocidade atual do carro? '))

if velocidade > 80:
    print('Você foi MULTADO!\nUltrapassou a velocidade permitida de 80km/h!\nO valor da multa é de: R$ {:.2f}' .format((velocidade - 80) * 7))
else:
    print('Você está dentro da velocidade permitida!')