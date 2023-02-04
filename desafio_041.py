import dateutil.utils

print('=' * 40)
txt = 'Desafio 041 - Classificando atletas'
print('\33[1:30:41m{:^40}\33[m'.format(txt))
print('=' * 40)

'''A confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre
sua categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JÚNIOR
- Até 25 anos: SÊNIOR
- Acima: MASTER'''

anoNascimento = int(input('ANO DE NASCIMENTO: '))
anoAtual = dateutil.utils.today().year
idade = anoAtual - anoNascimento

print('O atleta tem {} anos.' .format(idade))
if idade <= 9:
    print('MIRIM')
elif idade <= 14:
    print('INFANTIL')
elif idade <= 19:
    print('JÚNIOR')
elif idade <= 25:
    print('SÊNIOR')
else:
    print('MASTER')