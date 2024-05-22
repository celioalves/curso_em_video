# Crie um programa que leia o nome completo de uma pessoa e mostre o seguinte:
# O nome com todas as letras maiúsculas
# O nome com todas as letras minúsculas
# Quantas letras tem o nome, sem considerar os espaços
# Quantas letras tem o primeiro nome

nome = input('Digite seu nome completo:')
print(f'Esse é o nome minúsculo {nome.upper()}')
print(f'Esse é o nome maiúsculo {nome.lower()}')
nome2 = nome.strip()
letras = len(nome2)-nome.count(' ')
print(f'O nome tem {letras} caracteres, tirando os espaços')
nomeletras = nome.find(' ')
print(f'O seu primeiro nome tem {nomeletras} Letras')
print(f'O seu primeiro nome tem {len(nome.split()[1])} letras')
