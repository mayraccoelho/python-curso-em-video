print('=' * 40)
txt = 'Desafio 049 - Tabuada v.2.0'
print('\33[1:30:41m{:^40}\33[m'.format(txt))
print('=' * 40)

'''Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando o laço for.'''
numero = int(input('DIGITE NÚMERO PARA VER A TABUADA: '))
for i in range (0,11):
    print('{} x {:2} = {}' .format(numero, i, numero * i))