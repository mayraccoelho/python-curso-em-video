print('=' * 40)
txt = 'Desafio 001 - Respondendo ao Usuário'
print('\33[1:30:41m{:^40}\33[m'.format(txt))
print('=' * 40)

'''Crie um script Python que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas da acordo com o valor digitado.'''

nome = input('Qual é o seu nome? ')
print(f'Olá {nome}! Prazer em te conhecer!')