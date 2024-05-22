# desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.

primeiro = int(input('Qual número inicial? '))
razao = int(input('Qual o razão? '))
decimo_termo = primeiro + (10 - 1) * razao

for f in range(primeiro, decimo_termo + razao, razao):
    print(f'{f:.1f}')

