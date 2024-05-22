"""melhore o desafio 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
o programa encerra quando ele disser "zero" termos"""

print('Gerador de PA')
print('=-=' * 20)
primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = primeiro_termo
c = 1
total = 0
mais = 10

while mais != 0:
    total += mais
    while c <= total:
        print(f'{termo} -> ', end=' ')
        termo += razao
        c += 1
    print('PAUSA')
    mais = int(input('Quantos termos mais você deseja? '))
print(f'Programa finalizado, foram exibidos {total} termos')