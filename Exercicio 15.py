# Receba 2 notas de um aluno. Calcule a sua média e mostre se ele foi aprovado ou reprovado

nome = input('Digite o nome do aluno: \n')
nota = float(input('Digite a 1º nota: \n'))
nota2 = float(input('Digite a segunda nota: \n'))
media = (nota + nota2) / 2

if media >= 6:
    print('Aluno {} aprovado com nota {:.2f}!'.format(nome, media))
elif media < 6:
    print('Aluno {} reprovado com nota {:.2f}!'.format(nome, media))
