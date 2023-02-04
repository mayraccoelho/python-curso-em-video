print('=' * 40)
txt = 'Desafio 004 - Dissecando uma Variável'
print('\33[1:30:41m{:^40}\33[m'.format(txt))
print('=' * 40)

'''Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as possíveis informações sobre ele.'''

mensagem = input('Digite algo: ')

print('TIPO PRIMITIVO: ', type(mensagem))
print('SÓ TEM ESPAÇOS? ', mensagem.isspace())
print('NUMÉRICO: ', mensagem.isnumeric())
print('ALFABÉTICO: ', mensagem.isalpha())
print('ALFANUMÉRICO: ', mensagem.isalnum())
print('MAIÚSCULO: ', mensagem.isupper())
print('MINÚSCULO: ', mensagem.islower())
print('ESTÁ CAPITALIZADA? ', mensagem.istitle())


