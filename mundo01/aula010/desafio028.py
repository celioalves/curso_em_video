# escreva um programa que faça o computador 'pensar' um número inteiro entre 0 e 5 e peça para o
# usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu
from random import randint

print('-=-'*30)
print('Vou pensar em um número entre 0 e 100 para você tentar adivinhar...')
n = randint(0, 100)
c = int(input('Em qual número eu estou pensando? '))
print('-=-'*30)

if c == n:
    print('Parabéns você acertou')
else:
    print(f'Você errou, o número correto era {n}')
