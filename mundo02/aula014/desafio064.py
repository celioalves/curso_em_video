""" crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
No final, mostre quantos números foram digitados e qual foi a soma entre eles, desconsiderando o 999 """

soma = quantos = 0
n = int(input('Digite um valor: [999 para finalizar] '))
while n != 999:
    quantos += 1
    soma += n
    n = int(input('Digite um valor: [999 para finalizar] '))
print(f'Fim do programa. Foram digitados {quantos} números.'
      f' A soma entre eles foi de {soma}')
