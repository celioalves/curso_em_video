# Um professor quer sortear um dos seus 4 alunos para apagar o quadro.
# Faça um prograama que ajude ele, lendo o nome deles e escrevendo o nome escolhido
from random import choice

aluno1 = input('Digite o nome do Aluno 1 ')
aluno2 = input('Digite o nome do Aluno 2 ')
aluno3 = input('Digite o nome do Aluno 3 ')
aluno4 = input('Digite o nome do Aluno 4 ')

alunos = [aluno1, aluno2, aluno3, aluno4]

sorteado = choice(alunos)

print(f'Esses são os alunos {alunos}')
print('SORTEANDO...')
print(choice([f'O aluno sorteado foi o {sorteado}']))
