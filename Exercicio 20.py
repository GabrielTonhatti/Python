'''Considere que um carro faz 9km/litro de consumo com alcool. Já na gasolina ele faz 11km/litro. Faça um algoritmo em que o usuário irá
digitar a distância que deseja viajar, o preço do alcool e o preço do litro da gasolina. Calcule e mostre o valor que será gasto caso
abasteça com alcool e o valor gasto com gasolina. Mostre ainda se compensa abastecer com etanol ou com gasolina.'''

distancia = float(input('Qual distancia você deseja viajar? \n'))
Pgasolina = float(input('Qual o preço da gasolina?\n'))
Petanol = float(input('Qual o preço do etanol? \n'))
Letanol = float(distancia / 9)
Lgasolina = float(distancia / 11)
VGgasolina = float(Lgasolina * Pgasolina)
VGetanol = float(Letanol * Petanol)

print('O valor gasto caso abasteça com etanol é {:.2f}'.format(VGetanol))
print('O valor gasto caso abasteça com gasolina é {:.2f}'.format(VGgasolina))

if VGgasolina > VGetanol:
    print('Compensa abastecer com Etanol!')
else:
    print('Compensa abastecer com Gasolina!')