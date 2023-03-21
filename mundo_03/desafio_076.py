from prettytable import PrettyTable
tabela = PrettyTable()

print('=' * 40)
txt = 'Desafio 076 - Lista de Preços com Tupla'
print('\33[1:30:41m{:^40}\33[m'.format(txt))
print('=' * 40)

''' Crie um programa que tenha uma tupla única
com nomes de produtos e seus respectivos precos,
na sequência.
No final, mostre uma listagem de precos,
organizando os dados em forma tabular '''

produtos = (('Feijão', 5.60), ('Arroz', 20.90), ('Toddy', 15.60), ('Leite', 4.90), ('Azeite', 20.80))
tabela.field_names = ["Produtos", "Preço"]

for i in produtos:
    tabela.add_row(i)

print(tabela)