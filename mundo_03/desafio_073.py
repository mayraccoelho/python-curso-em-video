print('=' * 40)
txt = 'Desafio 073 - Tuplas com times de futebol'
print('\33[1:30:41m{:^40}\33[m'.format(txt))
print('=' * 40)

'''Crie uma tupla preenchida com os 20 primeiros colocados da tabela do Campeonato Brasileiro de Futebol, na ordem
de colocação. Depois mostre:
a) Apenas os 5 primeiros colocados.
b) Os últimos 4 colocados da tabela.
c) Uma lista com os times em ordem alfabético.
d) Em que posição da tabela está o time CHAPECOENCE.
OBS. novo d)Em que posição da tabela está o melhor time.'''

times_paulista = 'Palmeiras', 'São Paulo', 'CORINTHIANS', 'Bragantino', 'Ituano', 'Botafogo-SP', 'Mirassol', 'São Bernardo',\
                 'Guarani', 'Santo André', 'Ferroviária', 'Inter de Limeira', 'Água Santa', 'Santos', 'Ponte Preta', 'Novorizontino'

primeiros = times_paulista[:5]
print(f'Primeiros 5 colocados: {primeiros}')

ultimos = times_paulista[-4:]
print(f'Últimos 4 colocados: {ultimos}')

ordem_alfabetica = sorted(times_paulista)
print(f'Times em ordem alfabética: {ordem_alfabetica}')

posicao = times_paulista.index('CORINTHIANS')
print(f'O melhor time está na {posicao + 1}° posição!')
