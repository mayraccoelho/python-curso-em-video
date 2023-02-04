print('=' * 40)
txt = 'Desafio 024 - Verificando as primeiras letras de um texto'
print('\33[1:30:41m{:^40}\33[m'.format(txt))
print('=' * 40)

'''Crie um programa que leia o nome de uma cidade e diga se ela 
começa ou não com o nome "SANTO".'''

cidade = input('Em que cidade você nasceu? ')
dividirPalavra = cidade.split() # Ou cid[:5] == 'Santo'
palavraSanto = "SANTO" in dividirPalavra[0].upper()

print('Começa com Santo? {}' .format(palavraSanto))
