""" tuplas - são uma sequencia de objetos imutáveis, em outras palavras, uma vez criadas,
tuplas não podem ser modificadas, normalmente são usadas para guardar dados protegidos. São escritas entre (parênteses)
"""

print('EXEMPLOS: ')
linguagens = ('Python', 'Ruby', 'Java', 'JavaScript', 'Haskell')
print(linguagens)
print(type(linguagens))
print(linguagens[0].capitalize())
print(linguagens[1].upper())
print(linguagens[0:2])

for c in linguagens:
    print(c)
print('=-=' * 40)
