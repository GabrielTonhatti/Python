'''Peça para o usuário digitar um número representando as horas e outro número representando os minutos para hora de início de uma aula.
Depois peça para o usuário digitar um número da hora e outro número para o minuto do fim da aula. Mostre ao usuário quantos minutos a
aula durou'''

hora = int(input('Digite a hora que começou a aula: \n')) 
minutos = int(input('Digite os minutos que começou a aula: \n'))
horaf = int(input('Digite a hora que acabou a aula: \n'))
minutosF = int(input('Digite os minutos que acabou a aula: \n'))

total = minutos + minutosF + (hora * 60 + horaf * 60)

print('A aula durou {} minutos!'.format(total))