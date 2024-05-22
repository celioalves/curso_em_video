# escreva um programa que leia a velocidade de um carro.
# se ele ultrapassar 80 km/h, mostre uma mensagem dizendo que ele foi multado.
# a multa deve custar 7 reais por cada km acima do limite

velocidade = float(input('Qual a velocidade do carro? '))

if velocidade > 80:
    print(f'MULTA!!! o valor da multa é de R${(velocidade - 80) * 7:.2f}.')
else:
    print(f'O carro passou a {velocidade} e está dentro do permitido')
