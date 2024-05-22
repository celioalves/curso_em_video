# faça um programa que leia o peso de CINCO pessoas. No final, mostre qual foi o maior e o menor peso.

n = 1
pmax = 0
pmin = 0
lista = []

for x in range(0, 5):
    peso = float(input(f'Digite o peso da {n}ª pessoa: '))
    n += 1
    lista.append(peso)

print(f'O MAIOR peso lido foi de {max(lista)}Kg')
print(f'O MENOR peso lido foi de {min(lista)}Kg')
