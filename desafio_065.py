print('=' * 40)
txt = 'Desafio 065 - Maior e menor valores'
print('\33[1:30:41m{:^40}\33[m'.format(txt))
print('=' * 40)

'''Crie um programa que leia vários números inteiros pelo teclado.
No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
O programa deve perguntar ao usuário se ele quer continuar ou não continuar a digitar valores.'''

continuar = 'S'
maior = menor = cont = soma = media = 0

while continuar == 'S':
    n = int(input('Digite um número: '))
    continuar = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if cont == 0:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    soma += n
    cont += 1
media = soma / cont
print('-'*30)
print('Você digitou {} números.\nA média entre eles é: {:.2f}.\nO número maior é {} e o menor é {}.' .format(cont, media, maior, menor))
print('-'*30)
