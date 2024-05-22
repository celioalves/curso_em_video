n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a terceira nota: '))
n4 = float(input('Digite a quarta nota: '))

notaFinal = (n1 + n2 + n3 + n4) / 4

if notaFinal >= 6:
    print(f'Parabéns você alcançou a média {notaFinal:.2f} e foi aprovado de ano')
else:
    print(f'Infelizmente a sua média é de {notaFinal:.2f} e você reprovou')
