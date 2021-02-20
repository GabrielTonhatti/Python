'''Peça para o usuário digitar a sua altura e peso. Calcule o seu IMC através da fórmula (IMC = peso /(altura * altura)).
Mostre uma mensagem de que a pessoa está com o peso correto quando o IMC for menor que 25, e informe que está de sobrepeso
caso contrário'''

altura = float(input('Digite a sua altura: \n'))
peso = float(input('Digite o seu peso: \n'))
IMC = peso / (altura ** 2)

if IMC < 25:
    print('Você está no peso correto, seu IMC é {:.2f}'.format(IMC))
elif IMC > 25:
    print('Você está com sobrepeso, seu IMC é {:.2f}'.format(IMC))