#faça um programa que leia um número inteiro e diga se ele é primo ou não.

numero = int(input('Qual número você quer saber se é primo? '))
tot = 0
for c in range(1, numero + 1):
    if numero % c == 0:
        tot += 1
        print(f'{c}', end=' ')
if tot == 2:
    print('\nO número é primo')
else:
    print('\nnão é primo')
