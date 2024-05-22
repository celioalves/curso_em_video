"""
c = 1
while c < 11:
    print(c)
    c += 1
"""

from random import randint

random = randint(1, 5)
chute = 0

while chute != random:
    chute = int(input('Digite um valor para adivinhar: '))
    if chute > random:
        print('É UM NÚMERO MENOR')
    elif chute < random:
        print('É UM NÚMERO MAIOR')

if chute == random:
    print('PARABÉNS VOCÊ ACERTOU, FIM!!')
