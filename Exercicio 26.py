'''Peça çara o usuário digitar um número qualquer. Mostre se este número é positivo ou negativo, e se é par ou impar.
Para verificar se o número é par, o resto da divisão por 2 deverá ser 0. O resto da divisão em Python
é obtido através do operador %. resto = número % 2'''

n = int(input('Digite um número qualquer: \n'))
resto = n % 2

if resto == 0 and n > 0:
    print('O número {} é par e positivo!'.format(n))
elif resto == 0 and n < 0:
    print('O número {} é par e negativo!'.format(n))
elif resto != 0 and n > 0:
    print('O número {} é impar e positivo!'.format(n))
elif resto != 0 and n < 0:
    print('O número {} é impar e negativo!'.format(n))
elif n == 0:
    print('O número {} é neutro!'.format(n))
    