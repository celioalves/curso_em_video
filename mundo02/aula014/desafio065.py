"""Crie um programa que leia vários números inteiros pelo teclado.
No final da execução, mostre a média entre todos os valores, qual foi o menor e qual foi o maior dos lidos.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores."""

resp = 'Ss'
media = soma = quant = numMax = numMin = 0
listaN = []

while resp in 'Ss':
    num = int(input('Digite um valor: '))
    resp = input('Quer continuar? [S/N] ').strip().upper()[0]
    soma += num
    quant += 1
    listaN.append(num)
    numMax = max(listaN)
    numMin = min(listaN)

media = soma / quant
print(f'Você digitou {quant}, a soma foi de {soma} e a média é de {media}')
print(f'O menor valor digitado foi {numMin}, o maior foi {numMax}')
