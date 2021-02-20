# Faça um programa que receba o tempo em segundos de 3 voltas que um piloto de formula 1 percorreu. Mostre qual foi o mais rápido.

v = float(input('Digite o tempo em segundos da primeira volta: \n'))
v2 = float(input('Digite o tempo em segundos da segunda volta: \n'))
v3 = float(input('Digite o tempo em segundos da terceira volta:\n'))

if v < v2 and v < v3:
    print('A primeira volta foi mais rápida, com o tempo de  {}'.format(v))
elif v2 < v3:
    print('A segunda volta volta foi mais rápida, com o tempo de  {}'.format(v2))
else:
    print('A terceira volta foi mais rápida, com o tempo de  {}'.format(v3))