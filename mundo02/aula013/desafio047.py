# crie um programa que mostre todos os números pares que estão entre 1 e 50

for n in range(1, 51):
    if n % 2 == 0:
        print(n, end=' ')
print('acabou')
for n in range(2, 51, 2):
    print(n, end=' ')
