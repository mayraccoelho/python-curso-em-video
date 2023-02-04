print('=' * 40)
txt = 'Desafio 019 - Sorteando um item na lista'
print('\33[1:30:41m{:^40}\33[m'.format(txt))
print('=' * 40)

'''Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.'''

import random
lista = []
continuar = '1'

while continuar == '1':
    continuar = input('Quer adicionar um aluno?\nDigite 1 para SIM e 2 para NÃO: ')
    if continuar == '1':
        aluno = input('Nome do Aluno: ')
        lista.append(aluno)


print('==' * 20)
print('O ALUNO SORTEADO FOI: {}' .format(random.choice(lista)))
print('==' * 20)

