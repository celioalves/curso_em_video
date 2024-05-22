# faça um programa que calcule a soma entre todos os números ímpares que são multiplos de 3 e que se encontram no intervalo entre 1 e 500
# SÓ OS IMPARES MULTIPLOS DE 3 ENTRE 1 E 500
x = 0
cont = 0
for n in range(0, 500):
    if n % 3 == 0 and n % 2 != 0:
        cont += 1
        x += n

print(x)
print(cont)