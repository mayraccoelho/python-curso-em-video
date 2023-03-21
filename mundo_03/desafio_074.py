import random

print('=' * 40)
txt = 'Desafio 074 - Maior e menor valores em Tupla'
print('\33[1:30:41m{:^40}\33[m'.format(txt))
print('=' * 40)

''' Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.'''

tupla = tuple(random.sample(range(100), 5))
maior = tupla[0]
menor = tupla[0]

for i in range (0,5):
    if tupla[i] > maior:
        maior = tupla[i]
    elif tupla[i] < menor:
        menor = tupla[i]

print(f'Números gerados: {tupla}\nNúmero maior: {maior}\nNúmero menor: {menor}')

'''import random

tupla = tuple(random.sample(range(100), 5))  # gera cinco números aleatórios entre 0 e 100 e coloca em uma tupla

print("Listagem de números gerados:", tupla)
print("Maior valor na tupla:", max(tupla))
print("Menor valor na tupla:", min(tupla))
'''

'''CÓDIGO FUNCIONAL

import random

# Definir o tamanho da lista
TAMANHO_LISTA = 5

# Inicializar a lista com valores aleatórios
lista = [random.randint(0, 100) for _ in range(TAMANHO_LISTA)]

# Encontrar o maior e o menor valor da lista
maior = max(lista)
menor = min(lista)

# Converter a lista em uma tupla
tupla = tuple(lista)

# Imprimir os resultados
print(f'Lista de números: {tupla}\nMAIOR: {maior}\nMENOR: {menor}')
'''