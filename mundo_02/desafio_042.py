print('=' * 40)
txt = 'Desafio 042 - Analisando Triângulos v2.0'
print('\33[1:30:41m{:^40}\33[m'.format(txt))
print('=' * 40)

'''Refaça o desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
- EQUILÁTERO: Todos os lados iguais.
- ISÓSCELES: Dois lados iguais.
- ESCALENO: Todos os lados diferentes.'''

l1 = float(input('LADO 1: '))
l2 = float(input('LADO 2: '))
l3 = float(input('LADO 3: '))

if l1 + l2 > l3 and l2 + l3 > l1 and l3 + l1 > l2:
    print('Forma um triângulo ', end='')
    if l1 == l2 == l3:
        print('equilatero!')
    elif l1 != l2 != l3 != l1:
        print('escaleno!')
    else:
        print('isóceles!')
else:
    print('Não forma um triângulo!')


