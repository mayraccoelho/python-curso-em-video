print('=' * 40)
txt = 'Desafio 011 - Pintando Parede'
print('\33[1:30:41m{:^40}\33[m'.format(txt))
print('=' * 40)

'''\nFaça um programa que leia a largura e a altura de uma parede em metros, 
calcule a sua área e a quatidade de tinta necessária para pintá-la, 
sabendo que cada litro de tinta, pinta uma área de 2m².'''

largura = float(input('LARGURA: '))
altura = float(input('ALTURA: '))
area = largura * altura
tinta_necessaria = area / 2

print('LARGURA: {:.2f}\nALTURA: {:.2f}\nDIMENSÃO: {:.2f} x {:.2f}\nÁREA: {:.3f}m²\nTINTA NECESSÁRIA: {:.2f} litros' .format(largura, altura,largura, altura, area, tinta_necessaria))