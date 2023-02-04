print('=' * 40)
txt = 'Desafio 007 - Média Aritmética'
print('\33[1:30:41m{:^40}\33[m'.format(txt))
print('=' * 40)

'''Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua média.'''

n1 = float(input('Primeira nota do aluno: '))
n2 = float(input('Segunda nota do aluno: '))
media = (n1 + n2) / 2

print('A média do aluno é: {:.1f}' .format(media))