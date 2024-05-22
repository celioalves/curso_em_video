# faça um programa que mostra na tela uma contagem regressiva para o estouro de fogos de artifício,
# inde de 10 até 0, com uma pausa de um segundo entre eles
import time

for n in range(10, -1, -1):
    print(n)
    time.sleep(1)
print('FELIZ ANO NOVO!')
