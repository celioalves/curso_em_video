# escreva um progrma que leia um numero inteiro qualquer e peça para o usuário escolher qual será a base de conversao
# 1 - binário; 2 - octal; 3 - hexadecimal

n = int(input('Digite um número para efetuar a conversão: '))
opcao = int(input('Para o que você quer converter?\n[1] - Binário\n[2] - Octal\n[3] - hexadecimal\nDigite sua opção'
                  ' aqui  --> '))

if opcao == 1:
    binario = bin(n)
    print(binario.removeprefix('0b'))
elif opcao == 2:
    octal = oct(n)
    print(octal.removeprefix('0o'))
elif opcao == 3:
    hexadecimal = hex(n)
    print(hexadecimal.removeprefix('0x'))
else:
    print('Você digitou uma opção inválida')

