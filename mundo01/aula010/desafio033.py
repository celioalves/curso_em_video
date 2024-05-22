# faça um programa que leia três números e mostre qual é o maior e qual é o menor.
print('Digite três números para saber qual é o maior e o menor')

n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
n3 = float(input('Dígite o terceiro número: '))

lista = [n1, n2, n3]
print(f'O maior número digitado é {max(lista)}, e o menor é o {min(lista)}')
