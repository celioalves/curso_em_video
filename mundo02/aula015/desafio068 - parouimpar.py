from random import randint

# usuario

v = 0
while True:
    parouimpar = input('PAR OU ÍMPAR? [P/I]:').strip().upper()[0]
    while parouimpar not in 'PI':
        parouimpar = input('PAR OU ÍMPAR? [P/I]:').strip().upper()[0]
    numerojogador = int(input('ESCOLHA UM NÚMERO: '))
    while numerojogador > 10 or numerojogador < 0:
        print('VOCÊ DEVE JOGAR UM NÚMERO ENTRE 0 E 10')
        numerojogador = int(input('ESCOLHA UM NÚMERO: '))

    computador = randint(0, 10)
    print(f'o computador jogou {computador}')

    soma = numerojogador + computador

    print(f'Você jogou {numerojogador} e o computador {computador}.\n'
          f'Total de {soma}')

    if parouimpar == 'P':
        if soma % 2 == 0:
            print('DEU PAR, VOCÊ VENCEU')
            v += 1
        else:  # soma % 2 == 1:
            print('VOCÊ PERDEU')
            break
    if parouimpar == 'I':
        if soma % 2 == 1:
            print('DEU ÍMPAR, VOCÊ VENCEU')
            v += 1
        else:  # soma % 2 == 0:
            print('DEU PAR, VOCÊ PERDEU')
            break
if v > 1:
    print(f'Você ganhou {v} vezes seguidas, mas infelizmente sua sorte acabou')
elif v == 1:
    print(f'Você ganhou só {v} vez!')
else:
    print('Você não venceu nenhuma vez')
