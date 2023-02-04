print('=' * 40)
txt = 'Desafio 057 - Validação de Dados'
print('\33[1:30:41m{:^40}\33[m'.format(txt))
print('=' * 40)

'''Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores "M" ou "F".
Caso esteja errado, peça a digitação novamente até ter um valor correto.'''

sexo = str(input('Qual o sexo? [M/F]: ')).strip().upper()[0]
while sexo != 'M' and sexo != 'F': # ou while sexo not in 'MmFf':
    print('Pra continuar, por favor digitar "M" ou "F": ')
    sexo = input('Informe o sexo: [M/F] ').strip().upper()[0]

if sexo == "M":
    print('Você selecionou masculino.')
else:
    print('Você selecionou feminino.')
