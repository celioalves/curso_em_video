"""Escreva um programa que leia um número inteiro qualquer e mostre na tela os primeiros elementos de uma
sequencia fibonacci"""

numero = int(input('Quantos termos da sequência Fibonacci você quer mostrar: '))
t1 = 0
t2 = 1

print(f'{t1} -> {t2} ', end='')
cont = 3
while cont <= numero:
    t3 = t1 + t2
    print(f'-> {t3}', end=' ')
    cont += 1
    t1 = t2
    t2 = t3
print('-> Fim')
