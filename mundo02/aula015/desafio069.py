""" crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar se o usuário deseja continuar.
No final o programa deverá mostrar:
a) quantas pessoas tem mais de 18 anos
b) quantos homens foram cadastrados
c) quantas mulheres tem menos de 20 anos"""

lista_homens = lista_mulheres_menos_vinte = lista_dezoito = lista_pessoas = 0

while True:
    print('-*-' * 20)
    print('PREENCHA OS DADOS')
    print('-*-' * 20)
    idade = int(input('IDADE: '))
    lista_pessoas += 1
    if idade >= 18:
        lista_dezoito += 1
    sexo = ' '
    while sexo not in 'mf':
        sexo = input('SEXO - \n'
                     'M - MASCULINO\n'
                     'F - FEMININO:\n').strip().lower()[0]
    if sexo in 'm':
        lista_homens += 1
    elif sexo in 'f' and idade < 20:
        lista_mulheres_menos_vinte += 1
    continuar = ' '
    while continuar not in 'sn':
        continuar = input('Deseja continuar? [S/N]').strip().lower()[0]
    if continuar in 'n':
        break
print(f'{lista_pessoas} pessoas foram cadastradas, sendo que,\n'
      f'{lista_dezoito} pessoas tem mais de dezoito anos\n'
      f'{lista_mulheres_menos_vinte} mulheres tem menos de 20 anos\n'
      f'{lista_homens} homens foram cadastrados.')
