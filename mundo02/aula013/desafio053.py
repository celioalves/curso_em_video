#crie um programa que leia uma frase qualquer e diga se ela é um palíndromo. desconsiderando os espaços

frase = str(input('Digite a frase: ')).strip().upper()
print(f'Você digitou: {frase}')
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
"""inverso = ''

for letra in range(len(junto) - 1,  -1, -1):
    inverso += junto[letra]"""

'''print(inverso)'''

if inverso == junto:
    print('A FRASE É UM PALÍNDROMO')
else:
    print('NÃO É PALÍNDROMO')
