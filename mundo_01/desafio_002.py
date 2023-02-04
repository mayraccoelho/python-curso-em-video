print('=' * 40)
txt = 'Desafio 002 - Aniversário'
print('\33[1:30:41m{:^40}\33[m'.format(txt))
print('=' * 40)

'''Crie um script Python que leia o dia, o mês e ano do nascimento de uma pessoa e mostre uma mensagem com a data formatada'''

dia = input('DIA = ')
mes = input('MÊS = ')
ano = input('ANO = ')

print(f'Você nasceu no dia {dia}/{mes}/{ano}.')