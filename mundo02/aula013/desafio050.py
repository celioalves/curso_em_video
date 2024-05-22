#desenvolva um programa que leia 6 números inteiros e mostre a soma apenas daqueles que forem pares.
# Se o valor for ímpar, desconsidere-o
f = 0
for n in range(0, 6):
    x = int(input('Qual número você escolhe? '))
    if x % 2 == 0:
        f += x

print(f)
