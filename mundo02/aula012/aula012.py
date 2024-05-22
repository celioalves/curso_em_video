nome = input('Qual é o seu nome? ')
if nome == 'Gustavo':
    print('Que nome bonito')
elif nome == 'Célio':
    print('Seu nome é o mais bonito de todos')
elif nome == 'Maria' or nome == 'Pedro' or nome == 'Paulo':
    print('Seu nome é bem comum no Brasil.')
elif nome in 'Ana Cláudia Jéssica Juliana Bruna':
    print('É um bonito nome feminino')
else:
    print('Seu nome é bem normal')
print(f'Tenha um bom dia, {nome}')
