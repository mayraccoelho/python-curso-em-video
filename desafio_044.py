print('=' * 40)
txt = 'Desafio 044 - Gerenciador de Pagamentos'
print('\33[1:30:41m{:^40}\33[m'.format(txt))
print('=' * 40)

'''Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto.
- à vista cartão: 5% de desconto
- em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros'''

valorProduto = float(input('Preço das Compras: R$ '))
print('='*20)
print('''FORMAS DE PAGAMENTO
[1] à vista dinheiro/cheque
[2] à vista cartão
[3] em até 2x no cartão
[4] 3x ou mais no cartão''')
formaPagamento = int(input('Qual é a sua opção? '))
print('='*20)

if formaPagamento == 1:
    valorFinal = valorProduto - (valorProduto * 10 / 100)
    print('Sua compra terá 10% de desconto\nValor do Produto: R${:.2f}\nValor com desconto: R${:.2f}' .format(valorProduto, valorFinal))
elif formaPagamento == 2:
    valorFinal = valorProduto - (valorProduto * 5/100)
    print('Sua compra terá 5% de desconto\nValor do Produto: R${:.2f}\nValor com desconto: R${:.2f}' .format(valorProduto, valorFinal))
elif formaPagamento == 3:
    valorFinal = valorProduto
    parcela = valorProduto / 2
    print('Sua compra será parcelada em 2x\nValor do Produto: R${:.2f}\nValor parcelado em 2x: R${:.2f}' .format(valorProduto, parcela))
elif formaPagamento == 4:
    quantidadeParcelas = int(input('Quantas parcelas? '))
    valorComJuros = valorProduto + (valorProduto * 20/100)
    parcela = valorComJuros / quantidadeParcelas
    print('Compra parcelada em {}x de R${:.2f} COM JUROS\nValor do Produto: R${:.2f}\nValor com juros: R${:.2f}' .format(quantidadeParcelas, parcela, valorProduto, valorComJuros))
else:
    print('ESCOLHA INVÁLIDA')