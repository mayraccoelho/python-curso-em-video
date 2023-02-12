print('=' * 40)
txt = 'Desafio 072 - Número por extenso'
print('\33[1:30:41m{:^40}\33[m'.format(txt))
print('=' * 40)

'''Crie um programa que tenha uma tupla totalmente preenchida com uma 
contagem por extensão, de zero até vinte.
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.'''

contagem = 'zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', \
           'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte '


numero = int(input('Diga um número de 0 a 20: '))
for n in contagem:
    while numero < 0 or numero > 20:
        numero = int(input('Ops, algo deu errado.\nPor favor, digite um número entre 0 a 20: '))
    if numero == contagem.index(n):
        print(f'Você digitou o número {numero} ({n})')

