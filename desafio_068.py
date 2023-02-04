import random

print('=' * 40)
txt = 'Desafio 068 - Jogo Par ou Ímpar'
print('\33[1:30:41m{:^40}\33[m'.format(txt))
print('=' * 40)

'''Faça um programa que jogue par ou ímpar com o computador.
O jogo só será interrompido quando o jogador perder,
mostrando o total de vitórias consecutivas que ele conquistou, 
no final do jogo.'''

cont = 0

while True:
    nUsuario = int(input('Diga um número: '))
    nComputador = random.randint(0, 10)
    soma = nUsuario + nComputador
    tipo = ' '

    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I] ')).upper().strip()[0]

    print(f'Você jogou {nUsuario} e o computador {nComputador}. Total de {soma}. ', end='')
    print('Deu PAR!' if (soma) % 2 == 0 else 'Deu ÍMPAR!')

    if soma % 2 == 0:
        if tipo in 'Pp':
            print('Você GANHOU!')
            cont += 1
        else:
            print('Você PERDEU!')
            print('GAME OVER!', end='')
            break
    else:
        if tipo in 'Pp':
            print('Você PERDEU!')
            print('GAME OVER!', end='')
            break
        else:
            print('Você GANHOU!')
            cont += 1
print(f' Você venceu {cont} vez(es).')
