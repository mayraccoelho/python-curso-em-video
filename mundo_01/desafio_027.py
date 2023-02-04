print('=' * 40)
txt = 'Desafio 027 - Primeiro e último nome de uma pessoa'
print('\33[1:30:41m{:^40}\33[m'.format(txt))
print('=' * 40)

'''Faça um programa que leia o nome completo de uma pessoa,
mostrando em seguida o primeiro e o últimos nome separadamente.
Ex: Ana Maria de Souza
Primeiro = Ana
Último = Souza'''

nomeCompleto = input('Digite o seu nome completo: ').strip()
split = nomeCompleto.split(' ')
primeiro = split[0]
ultimo = split[-1] # ou nomeCompleto[len(nome) - 1]

print('PRIMEIRO NOME = {}\nÚLTIMO NOME = {}' .format(primeiro, ultimo))