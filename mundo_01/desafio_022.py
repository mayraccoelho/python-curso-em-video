print('=' * 40)
txt = 'Desafio 022 - Analisador de Textos'
print('\33[1:30:41m{:^40}\33[m'.format(txt))
print('=' * 40)

'''Crie um programa que leia o nome completo de uma pessoa e mostre:
O nome com todas as letras maiúsculas
O nome com todas as letras minúsculas
Quantas letras ao todo (sem considerar espaços)
Quantas letras tem primeiro nome'''

nome = str(input('Digite o seu nome: ')).strip()
maiuscula = nome.upper()
minuscula = nome.lower()
quantidadeLetras = len(nome.replace(' ', '')) # ou len(nome) - nome.count(' ')
splitNome = nome.split(' ')
quantidadeLetrasPrimeiroNome = len(splitNome[0]) # ou nome.find(' ') ele vai procurar índice do primeiro espaço, ou seja dará o numero correto de quantas letras tem primeiro nome

print('NOME: {}\n MAIUSCULA: {}\n MINUSCULA: {}\n QUANTIDADE DE LETRAS: {}\n QUANTIDADE DE LETRAS PRIMEIRO NOME: {}' .format(nome, maiuscula, minuscula, quantidadeLetras, quantidadeLetrasPrimeiroNome))