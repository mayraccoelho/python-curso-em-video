from datetime import date

print('=' * 40)
txt = 'Desafio 039 - Alistamento Militar'
print('\33[1:30:41m{:^40}\33[m'.format(txt))
print('=' * 40)

'''Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
- Se ele ainda vai se alistar ao serviço miliar.
- Se é hora de se alisar ao serviço militar.
- Se já passou do tempo de alistamento.

Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.'''

anoNascimento = int(input('ANO DE NASCIMENTO: '))
anoAtual = date.today().year
idade = anoAtual - anoNascimento

if idade < 18:
    print('Você ainda vai se alistar! Faltam {} ano(s).\nVocê se alista em {}' .format(18 - idade, anoAtual + (18 - idade)))
elif idade == 18:
    print('Estamos em {} e você deve se alistar imediatamente!' .format(anoAtual))
elif idade > 18:
    print('Você já passou do tempo de se alistar. Está {} ano(s) atrasado! Seu ano de alistamento foi em {}.' .format(idade - 18, anoAtual - (idade - 18)))
else:
    print('Escolha inválida')
