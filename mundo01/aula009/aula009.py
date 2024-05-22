frase = 'Curso em Vídeo Python'

print(len(frase))  # quantos caracteres tem na frase
print(frase.count('o'))  # quantos 'o' possuem na frase
print(frase.count('o', 0, 13))  # quantos 'o' possuem na frase, do caractere 0 ao 13
print(frase.find('deo'))  # em qual caractere começou a parte
# se retornar o valor -1 é que não existe
print('Curso' in frase)
print(frase[0:13:2])  # escreve a frase do caractere 0 ao 12, pulando de 2 em 2


print(frase.replace('Python', 'Android'))

print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())
print(frase.split())
print('-'.join(frase.split()))
print(''.join(frase.split()))

frase2 = '  Aprendendo Python   '
print(frase2)
print(frase2.strip())  # remove os espaços desnecessários de ambos os lados
print(frase2.lstrip())  # remove os espaços desnecessários da esquerda
print(frase2.rstrip())  # remove os espaços desnecessários da direita
