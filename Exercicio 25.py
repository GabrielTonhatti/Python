# Peça para o usuário digitar o nome de 2 times de futebol e a quantidade de gols que cada um deles fez. 
# Mostre o time campeão ou se houve.

time = input('Digite o nome do 1º time: \n')
time2 = input('Digite o nome do 2º time: \n')
gol = int(input('Quantos gols o {} fez? \n'.format(time)))
gol2 = int(input('Quantos gols o {} fez? \n'.format(time2)))

if gol > gol2:
    print('O time {} é o vencedor!'.format(time))
elif gol2 > gol:
    print('O time {} é o vencedor!'.format(time2))
elif gol == gol2:
    print('Houve um empate entre os dois times!')