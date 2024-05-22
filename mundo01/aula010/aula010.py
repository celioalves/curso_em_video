tempo = int(input('Quantos anos tem o seu carro?'))

if tempo <= 3:
    print('Seu carro está novo em folha')
else:
    print('Seu carro está velhinho')
print('--- FIM ---')


print('carro novo' if tempo <= 3 else 'carro velho')

nome = input('Qual o seu nome?')
if nome == 'Célio':
    print('Que nome lindo você tem')
else:
    print('Seu nome é tão normal')
print(f'Bom dia {nome}')
