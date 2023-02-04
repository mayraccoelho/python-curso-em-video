print('=' * 40)
txt = 'Desafio 026 - Primeira e última ocorrência de uma string'
print('\33[1:30:41m{:^40}\33[m'.format(txt))
print('=' * 40)

'''Faça um programa que leia uma frase pelo teclado e mostre:
Quantas vezes aparece a letra "A"
Em que posição ela aparece a primeira vez
Em que posição ela aparece a última vez'''

frase = input('Digite uma frase: ').strip().upper()
letraA = frase.count('A')
primeiroA = frase.find('A') + 1
ultimoA = frase.rfind('A') + 1 # Rfind procure a partir do lado direito

print('QUANTAS VEZES APARECE A LETRA "A"? {}\nÍNDICE DO PRIMEIRO "A": {}\nÍNDICE DO ÚLTIMO "A" {}' .format(letraA,primeiroA,ultimoA))

