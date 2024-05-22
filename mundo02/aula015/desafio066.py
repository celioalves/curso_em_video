""" Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
No final, mostre quantos números foram digitados e qual foi a soma entre eles."""

c = s = n = 0

while True:
    n = int(input('Digite um número: [999 p/ finalizar]'))
    if n == 999:
        break
    s += n
    c += 1
print(f'Foram {c} números digitados\n'
      f'A soma entre eles é de {s}')
print('Programa finalizado pelo usuário')
