# a confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua
# categoria de acordo com a idade: até 9 anos == mirim; até 14 anos == infantil; até 19 anos == júnior;
# até 25 anos == sênior; acima de 25 anos == master
from datetime import date

ano = int(input('Digite o ano do nascimento do atleta '))
idade = date.today().year - ano

if idade <= 9:
    print(f'O atleta tem {idade} anos e participa da categoria MIRIM')
elif idade <= 14:
    print(f'O atleta tem {idade} anos e participa da categoria INFANTIL')
elif idade <= 19:
    print(f'O atleta tem {idade} anos e participa da categoria JÚNIOR')
elif idade <= 25:
    print(f'O atleta tem {idade} anos e participa da categoria SÊNIOR')
else:
    print(f'O atleta tem {idade} anos e participa da categoria MASTER')
