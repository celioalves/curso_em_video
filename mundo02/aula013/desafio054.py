#crie um programa que leia o ano de nascimento de sete pessoas.
# no final, mostre quantas pessoas ainda não atingiram a maioridade (21 anos) e quantas já são maiores.

from datetime import date

ano = date.today().year
n = 1
maiores = 0
menores = 0
print(ano)
for x in range(0, 7):
    anonascimento = int(input(f'Digite o ano de nascimento da pessoa {n}ª:'))
    n += 1
    if ano - anonascimento >= 21:
        maiores += 1
    else:
        menores += 1

print(f'{maiores} são maiores de 21 anos')
print(f'{menores} são menores de 21 anos')
