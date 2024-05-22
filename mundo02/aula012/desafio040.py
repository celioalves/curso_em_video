# crie um programa que leia duas notas de um aluno e calculo a sua média, mostrando uma mensagem no final
# de acordo com a média atingida.
# abaixo de 5 == reprovado; entre 5 e 6.9 == recuperação; acima ou igual a 7 == aprovado

n1 = float(input('Digite a primeira nota do aluno: '))
n2 = float(input('Digite a segunda nota do aluno: '))

m = (n1 + n2) / 2

if m < 5:
    print(f'sua média foi {m}. Estude mais, você reprovou!')
elif m >= 7:
    print(f'Você foi aprovado, sua média foi {m}, parabéns!')
else:
    print(f'Sua média foi {m}. Você está de recuperação, tempo de estudar!')
