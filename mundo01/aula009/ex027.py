# faça um programa que leia o nome completo de uma pessoa,
# mostrando em seguido o primeiro e o ultimo nome, separadamente.
# ex: Ana Maria de Souza
# primeiro: Ana
# ultimo: Souza

nome = input('Digite seu nome completo').strip()

separa = nome.split(' ')

print(f'O primeiro nome é {separa[0].title()}')
print(f'O último nome é {separa[-1].title()}')