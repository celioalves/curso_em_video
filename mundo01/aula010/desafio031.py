# desenvolva um programa que pergunte a distância de uma viagem em km.
# Calcule o preço da passagem, cobrando R$ 0,50 por KM para viagens até 200km e R$ 0,45 para viagens mais longas

d = float(input('Para saber o preço da viagem digite a distância '))

if d > 200:
    print(f'A sua viagem custará R${d * 0.45:.2f}.')
else:
    print(f'A sua viagem terá um custo de R$ {d * 0.5:.2f}')
