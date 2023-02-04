print('=' * 40)
txt = 'Desafio 066 - Vários números com flag'
print('\33[1:30:41m{:^40}\33[m'.format(txt))
print('=' * 40)

'''Crie um programa que leia vários números inteiros pelo teclado
O programa só vai parar quando o usuário digitar 999,
que é a condição de parada (flag).
No final, mostre quantos números foram digitados
e qual foi a soma entre eles (desconsiderando o flag)'''

numero = soma = cont = 0

while True:
    numero = int(input('Digite um número [999 para parar]: '))
    if numero == 999:
        break
    soma += numero
    cont += 1

print(f'Você digitou {cont} números e a soma entre eles é de {soma}!')
