# elabore um programa que calculo o valor a ser pago por um produto, considerando o seu preço normal,
# e condição de pagamento.
# à vista no dinheiro / cheque == 10% de desconto
# à vista no cartão == 5% de desconto
# 2x no cartão == preço normal
# 3x ou mais no cartão == 20% de juros

preco_original = float(input('Qual o preço original do produto? '))
forma_de_pagamento = int(input('''Qual a forma de pagamento?
[1] à vista no dinheiro ou cheque
[2] à vista no cartão
[3] 2x no cartão
[4] 3x ou mais no cartão
Digite aqui --> '''))

if forma_de_pagamento == 1:
    print(f'10% de desconto!!! o que era R${preco_original} passou para {preco_original - (preco_original * 0.1)} ')
elif forma_de_pagamento == 2:
    print(f'5% de desconto!!! o que era R${preco_original} passou para R${preco_original - (preco_original * 0.05)} ')
elif forma_de_pagamento == 3:
    print(f'O preço se manteve o mesmo R${preco_original}')
else:
    print(f'Acréscimo de 20%. o preço subiu de {preco_original} para {preco_original * 1.2}')
