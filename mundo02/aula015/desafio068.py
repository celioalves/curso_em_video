""" faça um programa que jogue par ou ímpar com o computador.
O jogo só sera interrompido quando o jogador perder.
Mostrando um total de vitórias consecutivas que ele conquistou até o final do jogo"""

from random import randint

vitorias = 0

while True:
    opcao = ' '
    while opcao not in 'pi':
        opcao = input('PAR [P] / ÍMPAR [I]\n').strip().lower()[0]
    jogador = int(input('que número você escolhe? '))
    pc = randint(0, 10)
    soma = jogador + pc
    print(f'O computador escolheu {pc}, você escolheu {jogador}. a soma foi {soma}')
    if opcao in 'p':
        if soma % 2 == 0:
            print('Você venceu!!!')
            vitorias += 1
        else:
            print('Você perdeu')
            break

    if opcao in 'i':
        if soma % 2 == 1:
            print('Você venceu!!!')
            vitorias += 1
        else:
            print('Você perdeu')
            break
if vitorias > 0:
    print(f'Você venceu {vitorias} vezes seguidas')
else:
    print('Você não venceu nenhuma vez')
