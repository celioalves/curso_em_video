# aluguel de carro (diária = 60 R$, KM rodado = 0,15 R$)

dias = int(input('Por quantos dias o carro foi alugado? '))
kmrodado = float(input('Quantos Kms foram percorridos com o carro? '))

pagamentoCompleto = (dias * 60) + (kmrodado * 0.15)

print(f'O valor total por {dias} dias e {kmrodado} é de {pagamentoCompleto:.2f} reais')
