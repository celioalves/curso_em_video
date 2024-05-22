# faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade
# se ele ainda vai se alistar no exército. se é a hora de se alistar ou se já passou do tempo de alistamento.
# seu programa deverá mostrar o tempo que falta ou que passou do prazo para o alistamento
from datetime import date

ano_atual = date.today().year
ano = int(input('Qual seu ano de nascimento? '))
idade = ano_atual - ano
ano_de_alistamento = date.today().year - (idade - 18)

if idade > 18:
    print(f'Já passou do seu prazo de alistamento. Você deveria ter se alistado em {ano_de_alistamento}')
elif idade < 18:
    idade2 = 18 - idade
    print(f'Você tem {idade} anos. Faltam {idade2} anos para você se alistar')
else:
    print('Você deve se alistar esse ano')


