print('=' * 40)
txt = 'Desafio 025 - Procurando uma string dentro de outra'
print('\33[1:30:41m{:^40}\33[m'.format(txt))
print('=' * 40)

'''Crie um programa que leia o nome de uma pessoa e diga
se ela tem "SILVA" no nome.'''

nomeCompleto = input('Digite o seu nome completo: ').strip()
buscaNome = "SILVA" in nomeCompleto.upper()

print('Tem SILVA no nome? {}' .format(buscaNome))