print('=' * 40)
txt = 'Desafio 043 - Índice de Massa Corporal'
print('\33[1:30:41m{:^40}\33[m'.format(txt))
print('=' * 40)

'''Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status,
de acordo com a tabela abaixo:
- Abaixo de 18.5: Abaixo do peso
- Entre 18.5 e 25: Peso ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade Mórbida'''

peso = float(input('PESO (Kg): '))
altura = float(input('ALTURA (m): '))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é de {:.1f}' .format(imc))

if imc < 18.5:
    print('ABAIXO DO PESO')
elif imc >= 18.5 and imc < 25:
    print('PESO IDEAL')
elif imc >= 25 and imc < 30:
    print('SOBREPESO')
elif imc >= 30 and imc < 40:
    print('OBESIDADE')
elif imc >= 40:
    print('OBESIDADE MÓRBIDA')