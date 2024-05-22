# faça um programa que leia o sexo de uma pessoa, mas só aceite os valores M OU F. caso esteja errado, peça a digitação novamente até ter um valor correto

# opcao 1
'''print('ESCOLHA SUA OPÇÃO')
while True:
    sexo = input('Digite o sexo com M ou F: ').upper()
    if sexo == 'M':
        print(f'Você digitou a opção {sexo}')
        break
    elif sexo == 'F':
        print(f'Você digitou a opção {sexo}')
        break
    else:
        print('Opção inválida, tente novamente')'''

# opcao 2

sexo = input('Informe o seu sexo: [M/F] ').upper().strip()[0]
while sexo not in 'MmFf':
    sexo = input('''Dados inválidos, digite novamente
    --> ''').upper().strip()[0]
print(f'Sexo {sexo} registrado com sucesso')
