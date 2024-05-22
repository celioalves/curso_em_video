# refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora com o laço for

n1 = int(input('Qual número você quer saber a tabuada? '))
for x in range(1, 11):
    print(f'{n1} x {x} = {x*n1}')
