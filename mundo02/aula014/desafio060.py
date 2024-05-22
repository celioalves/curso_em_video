"""Faça um programa que leia um número qualquer e mostre seu fatorial
exemplo: 5! 5x4x3x2x1 = 120"""

"""from math import factorial
n = int(input('Digite um número para saber o seu fatorial: '))
f = factorial(n)
print(f'O fatorial de {n} é {f}')"""

from time import sleep

n = int(input('Digite um número para saber o seu fatorial: '))
c = n
f = 1
print(f'calculando {n}!...')
sleep(1)

while c > 0:
    print(f'{c}', end=' ')
    print('x' if c > 1 else '=', end=' ')
    f *= c
    c -= 1
print(f'{f}')