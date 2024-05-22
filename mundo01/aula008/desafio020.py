# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada para a apresentação.
from random import choice, sample

n1 = input('Digite o nome do primeiro aluno: ')
n2 = input('Digite o nome do segundo aluno: ')
n3 = input('Digite o nome do terceiro aluno: ')
n4 = input('Digite o nome do quarto aluno: ')

listaAlunos = [n1, n2, n3, n4]
sorteio = sample(listaAlunos, 4)

print(f'A ordem de apresentação é a seguinte: {sorteio} ')