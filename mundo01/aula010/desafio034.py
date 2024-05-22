# escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários maiores que R$ 1.250,00, calcule um aumento de 10%
# para salários menores ou iguais, o aumento é de 15%

salario = float(input('Para saber o aumento digite o salário atual? '))

if salario > 1250:
    print(f'O salário atual é de R$ {salario} e recebe um aumento de 10% '
          f'ficando em R${salario * 1.1:.2f}')
else:
    print(f'O salário atual é de R${salario} e recebe um aumento de 15% '
          f'ficando em R$ {salario * 1.15:.2f}')
