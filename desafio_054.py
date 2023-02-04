import datetime

print('=' * 40)
txt = 'Desafio 054 - Grupo de Maioridade'
print('\33[1:30:41m{:^40}\33[m'.format(txt))
print('=' * 40)

'''Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não
atingiram a maioridade e quantas já são maiores.'''
contadorMaior = 0
contadorMenor = 0

for i in range(1, 8):
    nascimento = int(input('Digite ano de nascimento da {}ª pessoa: ' .format(i)))
    idade = datetime.datetime.today().year - nascimento
    if idade >= 18:
        contadorMaior += 1
    else:
        contadorMenor += 1
print('Quantidade de pessoas maiores de idade: {}\nQuantidade de pessoas menores de idade: {}'.format(contadorMaior,
                                                                                                      contadorMenor))
