# Exercicio 16
#  peça para o usuário digitar o  seu ano de nascimento. Calcule a sua idade e mostre se ele pode entrar na balada ou não.
# Menores de 18 anos não entram na balada.

nome = input('Qual seu nome? \n')
nascimento = int(input('Qual seu ano de nascimento?\n'))
anoatual = int(input('Qual o ano atual?\n'))
idade = anoatual - nascimento

if idade >= 18:
    print('Você tem {} anos, você pode entrar na balada!'.format(idade))
elif idade < 18:
    print('Você tem {} anos, você não pode entrar salafraio!'.format(idade))