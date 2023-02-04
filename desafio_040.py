print('=' * 40)
txt = 'Desafio 040 - Aquele clássico de média'
print('\33[1:30:41m{:^40}\33[m'.format(txt))
print('=' * 40)

'''Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo 
com a média atingida:
- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 o superior: APROVADO'''

nota1 = float(input('NOTA 1: '))
nota2 = float(input('NOTA 2: '))
media = nota1 / nota2

if media <= 5:
    print('REPROVADO')
elif 5 < media < 7:
    print('RECUPERAÇÃO')
elif media >= 7:
    print('APROVADO')

