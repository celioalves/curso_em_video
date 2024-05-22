# crie um programa que faça o computador jogar jokenpô com você
from random import randint
import time

itens = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0,2)

jogador = int(input('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA
Escolha a jogada --> '''))
if jogador != 0 and jogador != 1 and jogador != 2:
    print('Jogada inválida')

else:
    print('PEDRA, PAPEL OU TESOURA...')
    print('ESCOLHENDO...')
    time.sleep(2)
    print('-=-' * 20)
    print(f'Computador escolheu {itens[computador]}')
    print(f'Jogador escolheu {itens[jogador]}')
    print('-=-' * 20)

    frase1 = 'EMPATOU'
    frase2 = 'O JOGADOR VENCEU'
    frase3 = 'O COMPUTADOR VENCEU'

if computador == 0:
    if jogador == 0:
        print(frase1)
    elif jogador == 1:
        print(frase2)
    elif jogador == 2:
        print(frase3)
    else:
        print('Opção inválida, tente novamente')

elif computador == 1:
    if jogador == 0:
        print(frase3)
    elif jogador == 1:
        print(frase1)
    elif jogador == 2:
        print(frase2)
    else:
        print('Opção inválida, tente novamente')

elif computador == 2:
    if jogador == 0:
        print(frase2)
    elif jogador == 1:
        print(frase3)
    elif jogador == 2:
        print(frase1)
    else:
        print('Opção inválida, tente novamente')






