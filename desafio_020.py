print('=' * 40)
txt = 'Desafio 020 - Sorteando uma ordem na lista'
print('\33[1:30:41m{:^40}\33[m'.format(txt))
print('=' * 40)

'''O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. 
Faça um programa que leia o nome dos quatros alunos e mostre a ordem sorteada.'''

import random
from time import sleep

lista = []
continuar = '1'

while continuar == '1':
    continuar = input('Quer adicionar um aluno?\nDigite 1 para SIM e 2 para NÃO: ')
    if continuar == '1':
        aluno = input('Nome do Aluno: ')
        lista.append(aluno)

print('Processando...')
sleep(2)

print('==' * 20)
print('A ORDEM DE APRESENTAÇÃO É: {}' .format(random.sample(lista, len(lista)))) #função shuffle foi descontinuado
print('==' * 20)

