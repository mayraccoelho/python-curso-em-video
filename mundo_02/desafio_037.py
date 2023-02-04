print('=' * 40)
txt = 'Desafio 037 - Conversor de Bases Númericas'
print('\33[1:30:41m{:^40}\33[m'.format(txt))
print('=' * 40)

'''Escreva um programa que leia um número inteiro qualquer e peça para o usuário
escolher qual será a base de conversão:
- 1 para binário
- 2 para octal
- 3 para hexadecimal'''

numero = int(input('Digite um número: '))
escolha = int(input('\nDeseja converter para qual base?'
      '\n[1] - Binário'
      '\n[2] - Octal'
      '\n[3] - Hexadecimal'
    '\nSelecione a opção desejada: '))

if escolha == 1:
    print(bin(numero)[2:])
elif escolha == 2:
    print(oct(numero)[2:])
elif escolha == 3:
    print(hex(numero)[2:])
else:
    print('Escolha inválida')