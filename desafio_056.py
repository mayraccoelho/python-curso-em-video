from pprint import pprint

print('=' * 40)
txt = 'Desafio 056 - Analisador Completo'
print('\33[1:30:41m{:^40}\33[m'.format(txt))
print('=' * 40)

'''Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: 
- A média de idade do grupo.
- Qual é o nome do homem mais velho.
- Quantas mulheres tem menos de 20 anos.'''

pessoas = {'nome':'', 'idade':'', 'sexo':''}
mediaIdade = 0
nomeHomemMaisVelho = ''
idadeMaisVelho = 0
mulheresMenos20 = 0
nomeMulher = ''

for i in range (1, 5):
    print('=-=-=- {}ª PESSOA -=-=-=' .format(i))
    nome = str(input('NOME: ' .format(i)))
    idade = int(input('IDADE: ' .format(i)))
    sexo = str(input('SEXO [F/M]: ' .format(i)))

    mediaIdade += idade/4

    if i == 1 and sexo in 'Mm':
        nomeHomemMaisVelho = nome
        idadeMaisVelho = idade
    else:
        if sexo in 'Mm' and idade > idadeMaisVelho:
            nomeHomemMaisVelho = nome
            idadeMaisVelho = idade

    if idade < 20 and sexo in 'Ff':
        mulheresMenos20 += 1

print('A média do grupo é de: {} anos' .format(mediaIdade))
print('Homem mais velho é o {} que tem {} anos. ' .format(nomeHomemMaisVelho, idadeMaisVelho))
print('{} mulher(es) tem menos de 20 anos. ' .format(mulheresMenos20))

