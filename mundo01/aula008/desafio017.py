# faça um programa que leia o cateto oposto e do cateto adjacente de um triângulo retângulo,
# calcule e mostre o cumprimento da hipotenusa
from math import hypot

ladoA = float(input('Digite o cateto oposto. Ex. 3.56: '))
ladoB = float(input('Digite o cateto adjacente: '))
hipotenusa = hypot(ladoA, ladoB)

print(f'A hipotenusa vai medir {hipotenusa:.2f}')