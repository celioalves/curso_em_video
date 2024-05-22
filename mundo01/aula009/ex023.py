# faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados
# ex: 1834 - unidade 4 dezena 3 centenaa 8 milhar 1

numero = input('Digite seu número: ')

print(f'Unidade: {numero[3]}')
print(f'Dezena: {numero[2]}')
print(f'Centena: {numero[1]}')
print(f'milhar: {numero[0]}')
