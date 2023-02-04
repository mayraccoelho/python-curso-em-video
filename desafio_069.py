print('=' * 40)
txt = 'Desafio 069 - Análise de dados do grupo'
print('\33[1:30:41m{:^40}\33[m'.format(txt))
print('=' * 40)

'''Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar
se o usuário quer ou não continuar.
No final, mostra:
a) quantas pessoas têm mais de 18 anos
b) quantos homens foram cadastrados
c) quantas mulheres têm menos de 20 anos'''


maior18 = homens = mulheres = 0
while True:
    sexo = ' '
    continuar = ' '

    print('=-' * 10)
    print('CADASTRE UMA PESSOA')
    print('=-' * 10)

    idade = int(input('IDADE: '))

    while sexo not in 'FM':
        sexo = str(input('SEXO: [F/M] ')).upper().strip()[0]

    if idade >= 18:
        maior18 += 1
    if sexo in 'Mm':
        homens += 1
    if sexo in 'Ff' and idade < 20:
        mulheres += 1

    while continuar not in 'SN':
        continuar = str(input('DESEJA CONTINUAR? [S/N]')).upper().strip()[0]

    if continuar in 'Nn':
        print('\n======= FIM PROGRAMA =======\n')
        print(f'{maior18} pessoas tem mais de 18 anos\n{homens} homens foram cadastrados\n{mulheres} mulheres tem menos de 20 anos.')
        break