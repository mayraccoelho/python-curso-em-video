print('=' * 40)
txt = 'Desafio 064 - Tratando vários valores v1.0'
print('\33[1:30:41m{:^40}\33[m'.format(txt))
print('=' * 40)

'''Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999,
que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma
entre eles (desconsiderando o flag 999!)'''

n = soma = 0
cont = -1

while n != 999:
    n = int(input('Digite um número [999 para sair]: '))
    if n != 999:
        soma += n
    cont += 1
print('Você digitou {} números e a soma entre eles foi {}!' .format(cont, soma))