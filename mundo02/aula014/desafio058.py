"""melhore o jogo do desafio 028 onde o computador vai "pensar" em um número de 0 a 10.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários
para vencer"""

from random import randint

chute = int
numero = randint(0, 10)
tentativas = 0

while chute != numero:
    chute = int(input('TENTE ADIVINHAR O NÚMERO DE 0 A 10\n'))
    if chute > numero:
        print('O número que eu pensei é menor')
    elif chute < numero:
        print('O número que eu pensei é maior')
    tentativas +=1
else:
    print(f'Exaaaaato! o número que eu tinha pensado era {numero}')
    print(f'Você acertou em {tentativas} tentativas!')
