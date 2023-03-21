print('=' * 40)
txt = 'Desafio 075 - Análise de dados em uma Tupla'
print('\33[1:30:41m{:^40}\33[m'.format(txt))
print('=' * 40)

'''Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final mostre:
1 - Quantas vezes apareceu o valor 9.
2 - Em que posição foi digitado o primeiro valor 3.
3 - Quais foram números pares.'''

lista = []
lista_pares = []
valor3 = 0

for i in range (1,5):
    try:
        valor = int(input(f'Digite {i}º valor: '))
        if valor % 2 == 0:
            lista_pares.append(valor)
        lista.append(valor)
    except ValueError:
        print('Valor inválido, digite um número inteiro.')
        i -= 1

valor = tuple(lista)
valor9 = valor.count(9)
if 3 in valor:
    valor3 = valor.index(3) + 1
else:
    valor3 = 'Nenhuma vez'

print(f'Quantas vezes apareceu o valor 9: {valor9}')
print(f'Em que posição foi digitado o primeiro valor 3: {valor3}')
print(f'Quais foram números pares: {lista_pares}')
