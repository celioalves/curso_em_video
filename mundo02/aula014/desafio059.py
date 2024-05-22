"""crie um programa que leia dois valores e mostre um meno na tela
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa
seu programa deverá realizar a operação solicitada em cada caso"""

v1 = float(input('Digite o primeiro valor: '))
v2 = float(input('Digite o segundo valor: '))

opcao = 0

while opcao != 5:
    print('''Qual opção você deseja? 
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa
    ''')
    opcao = int(input('Qual sua opção? --> '))
    if opcao == 4:
        print('Digite os novos valores')
        v1 = float(input('Digite o primeiro valor: '))
        v2 = float(input('Digite o segundo valor: '))
    if opcao == 1:
        print(f'O resultado da soma é {v1 + v2}')
    elif opcao == 2:
        print(f'O resultado da multiplicação é {v1 * v2}')
    elif opcao == 3:
        if v1 > v2:
            print(f'O primeiro valor ({v1}) é maior que o segundo ({v2})')
        elif v2 > v1:
            print(f'O segundo valor ({v2}) é maior que o primeir ({v1})')
        else:
            print(f'Os valores {v1} e {v2} são iguais')
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente')
    print('=-=' * 10)
print('Fim do programa')
