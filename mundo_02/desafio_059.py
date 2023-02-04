from time import sleep

print('=' * 40)
txt = 'Desafio 059 - Criando Menu de Opções'
print('\33[1:30:41m{:^40}\33[m'.format(txt))
print('=' * 40)

'''Crie um programa que leia dois valores e mostre um menu na tela:
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.'''

n1 = int(input('PRIMEIRO NÚMERO: '))
n2 = int(input('SEGUNDO NÚMERO: '))
opcao = 0

while opcao != '5':
    print('=-=-=- MENU -=-=-=')
    print('''[1] somar\n[2] multiplicar\n[3] maior\n[4] novos números\n[5] sair do programa''')
    opcao = input('Selecione a opção desejada: ')

    if opcao == '1':
        print('=-=-=- SOMA -=-=-=')
        print('{} + {} = {}' .format(n1,n2,n1+n2))
        print('=-=-=--=-=-=')
        sleep(1)
    elif opcao == '2':
        print('=-=-=- MULTIPLICAÇÃO -=-=-=')
        print('{} * {} = {}' .format(n1,n2,n1*n2))
        print('=-=-=--=-=-=')
        sleep(1)
    elif opcao == '3':
        print('=-=-=- MAIOR NÚMERO -=-=-=')
        if n1 > n2:
            print('O {} é maior que {}.' .format(n1,n2))
        elif n2 > n1:
            print('O {} é maior que {}.' .format(n2,n1))
        else:
            print('Os números são iguals!')
        print('=-=-=--=-=-=')
        sleep(1)
    elif opcao == '4':
        print('=-=-=- DIGITAR NÚMEROS NOVAMENTE -=-=-=')
        n1 = int(input('PRIMEIRO NÚMERO: '))
        n2 = int(input('SEGUNDO NÚMERO: '))
        print('=-=-=--=-=-=')
        sleep(1)
    elif not 5:
        print('=-=-=- OPÇÃO INVÁLIDA. TENTE NOVAMENTE -=-=-=')
        sleep(1)

print('Processando...')
sleep(2)
print('ENCERRADO')
