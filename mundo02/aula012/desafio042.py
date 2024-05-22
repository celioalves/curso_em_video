# refaça o desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# equilátero = todos os lados são iguais;
# isósceles = dois lados iguais;
# escaleno = todos os lados diferentes;


a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))


if a < b + c and b < a + c and c < b + a:
    print('PODEM formar um triângulo', end=' ')
    if a == b == c:
        print('EQUILÁTERO')
    elif a == b or b == c or c == a:
        print('ISÓSCELES')
    elif a != b != c != a:
        print('ESCALENO')
else:
    print('NÃO podem formar um triângulo')
