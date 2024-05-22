# Faça um programa que leia um ângulo qualquer e mostre na tela o valor de seno, cosseno e tangente desse ângulo
from math import cos, sin, tan, radians

ang = float(input('Digite o ângulo para saber o Seno, Cosseno e Tangente: '))
s = sin(radians(ang))
c = cos(radians(ang))
t = tan(radians(ang))

print(f'Para o ângulo {ang:.3f}º\nO valor do Seno é de {s:.3f}\nO Cosseno é de {c:.3f}\nA Tangente é de {t:.3f}.')
