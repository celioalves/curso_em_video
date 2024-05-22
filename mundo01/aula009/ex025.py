# crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome
nome = input('Digite seu nome completo:').strip()
maiusculo = nome.upper()
print('SILVA' in maiusculo)