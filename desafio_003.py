print('=' * 40)
txt = 'Desafio 003 - Somando dois números'
print('\33[1:30:41m{:^40}\33[m'.format(txt))
print('=' * 40)

'''Crie um script Python que leia dois números e tente mostrar a soma entre eles'''

def soma():
    a = int(input('Digite o primeiro número: '))
    b = int(input('Digite o segundo número: '))
    return print('A soma é:', a + b)

soma()