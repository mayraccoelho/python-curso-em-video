print('=' * 40)
txt = 'Desafio 055 - Maior e Menor de sequência'
print('\33[1:30:41m{:^40}\33[m'.format(txt))
print('=' * 40)

'''Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos'''

for i in range(1,6):
    peso = float(input('Digite o peso da {}ª pessoa: ' .format(i)))
    if i == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print('Maior peso é: {}Kgs\nMenor peso é: {}Kgs' .format(maior, menor))
