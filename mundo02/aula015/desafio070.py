""" Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário quer
continuar. No final, mostre:
A) qual o total gasto na compra
B) quantos produtos custam mais de 1000 reais
C) QUAL O NOME DO PRODUTO MAIS BARATO"""

print('*_*' * 25)
print('LOJAS SALDÃO')
print('*-*' * 20)

menor = total = mais_de_mil = cont = 0
nome_produto_barato = ' '
produto_barato_preco = 0


while True:
    print('----' * 5)
    produto = input('Nome do produto: ')
    cont += 1
    preco = float(input('Preço: R$ '))
    if preco > 1000:
        mais_de_mil += 1
    total += preco
    if cont == 1 or preco < menor:
        menor = preco
        nome_produto_barato = produto
    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Deseja continuar? [S/N]').strip().upper()[0]
    if continuar == 'N':
        break
print(f'O total da compra foi de {total:.2f} reais.')
print(f'O produtor mais barato foi {nome_produto_barato} que custou {menor:.2f} reais')
print(f'{mais_de_mil} produto(s) custou mais de R$ 1.000,00')
