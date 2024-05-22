""" Crie um programa que simule o funcionamento de um caixa eletronico. No início pergunte ao usuário qual
será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues

OBS: considere que o caixa possui cédulas de R$ 50, 20, 10 e 1"""


"""saque1 = int(input('DIGITE O VALOR QUE DESEJA SACAR: '))
n50 = n20 = n10 = n1 = 0
saque = saque1
while True:

    if saque >= 50:
        saque -= 50
        n50 += 1
    else:
        if saque >= 20:
            saque -= 20
            n20 += 1
        else:
            if saque >= 10:
                saque -= 10
                n10 += 1
            else:
                if saque >= 1:
                    saque -= 1
                    n1 += 1
    if saque == 0:
        break
print(f'O total do saque foi de {saque1}, dividido em:'
      f' {n50} notas de R$ 50, {n20} notas de R$ 20, {n10} notas de R$ 10 e {n1} notas de R$ 1')



solução guanabara"""

valor = int(input('Qual valor você quer sacar? '))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
