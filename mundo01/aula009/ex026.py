# faça um programa que leia uma frase pelo teclado e mostre:
# quantas vezes aparece a letra "a"
# em que posição a letra "a" aparece pela primeira vez
# em que posição ela aparece pela última vez

frase2 = input('Digite uma frase: ').strip()
frase = frase2.lower()
print(frase.count('a'))
print(frase.find('a')+1)
print(frase.rfind('a')+1)
