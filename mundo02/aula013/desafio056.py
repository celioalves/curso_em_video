# desenvolva um programa que leia o nome, idade e sexo de 4 pessoas e no final mostre:
# a média de idade do grupo
# qual o nome do homem mais velho
# quantas mulheres tem menos de 21 anos.
n = 1
somaidade = 0
maior_idade_homem = 0
nome_velho = ''
totmulher20 = 0

for x in range(0, 4):
    nome = input(f'Digite o nome da {n}ª pessoa: ')
    idade = int(input(f'Digite a idade de {nome}: '))
    somaidade += idade
    n += 1
    sexo = int(input(f'Qual o sexo de {nome}: \n1 - Masculino\n2 - Feminino\nDigite aqui -->'))
    if x == 1 and sexo == 1:
        maior_idade_homem = idade
        nome_velho = nome
    if sexo == 1 and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_velho = nome
    if sexo == 2 and idade < 20:
        totmulher20 += 1

print(f'O homem mais velho se chama {nome_velho} e tem {maior_idade_homem} anos.')
print(f'A média de idade do grupo é de {somaidade/4} anos')
print(f'Ao todo são {totmulher20} mulher com menos de 20 anos')