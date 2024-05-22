# desenvolva um programa que leia o comprimento de três retas e
# diga ao usuário se elas podem ou não formar um triângulo
# cada um dos segmentos deve ser menor que a soma dos outros dois segmentos

a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))

if a < b + c and b < a + c and c < b + a:
    print('PODEM formar um triângulo')
else:
    print('NÃO podem formar um triângulo')
