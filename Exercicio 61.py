# 61 - Elabore um programa que peça para o usuário digitar 10 número inteiros.
# Caso seja digitado um número repetido, o sistema deve avisar ao usuário,
# porém pode aceitar esse numero assim mesmo. Depois exiba os 10 numeros
# digitados.
# altere o algorítmo para que além de avisar sobre números repetidos, peça para
# o usuário digitar novamente impedindo que se tenha números repetidos.

num = []

for i in range(1, 11):
    num = input('Digite o {}º número! \n'.format(i))
    for j in range(1, i):
        if num[j] == num[i] and i != j:
            print('O número {} já foi digitado!'.format(num[i]))
