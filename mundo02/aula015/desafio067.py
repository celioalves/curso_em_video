from time import sleep

print('PARA SAIR DIGITE UM NÚMERO NEGATIVO')
while True:
    n = int(input('Digite um número para saber a tabuada: '))
    if n < 0:
        break
    for t in range(1, 11):
        print(f'{n} x {t} = {n*t} ||', end=' ')

print('Finalizando...')
sleep(1)
print('Programa finalizado com sucesso')

""" PROGRAMA TABUADA - DIGITE UM NÚMERO PARA SABER A TABUADA, E PARA SAIR DIGITE UM NEGATIVO """
