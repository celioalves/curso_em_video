n = cont = s = 0

while True:
    n = int(input('Digite um número '))
    if n == 999:
        break
    s += n
    cont += 1

print(f'Foram digitados {cont} números, resultando na soma de {s}')
print('Fim')
