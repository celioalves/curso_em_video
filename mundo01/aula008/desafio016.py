# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.
from math import trunc

num = float(input('Digite um número real: '))
parteInteira = trunc(num)

print(f'A parte inteira de {num}  é {parteInteira}')
