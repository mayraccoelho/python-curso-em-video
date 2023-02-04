print('=' * 40)
txt = 'Desafio 070 - Estatísticas em produtos'
print('\33[1:30:41m{:^40}\33[m'.format(txt))
print('=' * 40)

'''Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar.
No final, mostre:
a) qual é o total gasto na compra
b) quantos produtos custam mais de R$ 1000
c) qual é o nome do produto mais barato'''

total = cont = produtos1000 = menor = 0
nomeMenor = ''

while True:
    continuar = ' '

    print('=-' * 5)
    print('LISTA DE COMPRAS')
    print('=-' * 5)

    nome = str(input('PRODUTO: ')).upper()
    preco = float(input('PREÇO: R$'))

    while continuar not in 'SN':
        continuar = str(input('DESEJA CONTINUAR? [S/N]')).upper().strip()[0]

    total += preco
    if cont == 0:
        menor = preco
    if preco <= menor:
        nomeMenor = nome
        menor = preco
    if preco > 1000:
        produtos1000 += 1

    if continuar in 'Nn':
        print('====== PROGRAMA ENCERRADO ======')
        break

    cont += 1

print(f'\nTOTAL GASTO: R${total:.2f}\nQUANTIDADE DE PRODUTOS QUE CUSTAM MAIS DE R$1000,00: {produtos1000}\nPRODUTO MAIS BARATO: {nomeMenor} QUE CUSTA R${menor:.2f}')
