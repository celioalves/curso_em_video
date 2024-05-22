# desenvolva uma lógica que leia o peso e altura de uma pessoa, calcule seu imc e mostre seu status,
# de acordo com a tabela: abaixo de 18.5 == abaixo do peso; entre 18.5 e 25 == peso ideal;
# 25 a 30 == sobrepeso; 30 a 40 == obesidade e 40+ == obesidade mórbida

a1 = int(input('Qual a sua altura em centímetros? '))
p = float(input('Qual o seu peso em kg? '))

a = a1 / 100

imc = p / a**2

print(f'{imc:.2f}')

if imc <= 18.5:
    print('Você está abaixo do peso')
elif imc <= 25:
    print('Você está no peso ideal')
elif imc <= 30:
    print('Você está com sobrepeso')
elif imc <= 40:
    print('Você está com obesidade')
else:
    print('Você está com obesidade morbida')

