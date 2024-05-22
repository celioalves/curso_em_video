# escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# o programa vai perguntar o valor da casa, o salário do comprador e em quantos anos vai pagar.
# calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário, ou o empréstimo será negado.

print('=-='*20)
valorCasa = float(input('Qual o valor do imóvel? R$ '))
salario = float(input('Qual o valor do salário? R$ '))
anos = int(input('Em quantos anos você pretende pagar a casa? '))
print('=-='*20)

meses = anos * 12
prestacao = valorCasa / meses
print(f'A prestação fica um valor de R$ {prestacao:.2f}')

if prestacao > (salario * 0.3):
    print(f'Infelizmente a prestação em {meses} meses, '
          f'excede 30% do salário (que é R$ {salario * 0.3}), empréstimo NEGADO!!!')
else:
    print(f'A {prestacao:.2f} está dentro do permitido, empréstimo APROVADO!!!')