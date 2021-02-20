'''Um aluno é aprovado apenas quando tem média de suas notas maior ou igual à 6 e quando tem menos que 20 faltas. Peça para o usuário
digitar suas 2 notas e a quantidade de faltas e mostre se ele está aprovado ou não.'''

name = input('Qaul é o seu nome? \n')
nota = float(input('Digite a sua primeira nota: \n'))
nota2 = float(input('Digite a sua segunda nota: \n'))
faltas = int(input('Digite a quantidade de faltas que você tem: \n'))
media = (nota + nota2) / 2

if media >= 6 and faltas < 20:
    print('{}, você está aprovado com {} de média, você teve {} faltas!'.format(name, media, faltas))
elif media < 6 and faltas < 20:
    print('{}, você está reprovado por conta da sua nota, você fechou com {} de média, você teve {} faltas!'.format(name, media, faltas))
elif media >= 6 and faltas >= 20:
    print('{}, você está reprovado por conta das faltas, você teve {} faltas e {} de média!'.format(name, faltas, media))
elif media < 6 and faltas >= 20:
     print('{}, você está reprovado por conta da média e das faltas, com {} de média e {} faltas!'.format(name, media, faltas))