print('=' * 40)
txt = 'Desafio 067 - Tabuada v3.0'
print('\33[1:30:41m{:^40}\33[m'.format(txt))
print('=' * 40)

'''Faça um programa que mostre a tabuada de vários números,
um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo'''

while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n < 0:
        print('==== PROGRAMA ENCERRADO ====')
        break
    print(f'==== TABUADA DO {n} ====')
    for i in range (0,11):
        print(f'{n} x {i} = {n*i}')
    print('=' *20)


