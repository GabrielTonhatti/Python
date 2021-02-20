'''Peça para o usuário digitar se ele tem febre alta, manchas na pele e dor no corpo. Faça um algoritmo capaz de dar o diagnóstico 
para as pessoas seguindo a tabela fictícia:
Dengue: Febre Alta + Dor no Corpo
Zika: Manchas na Pele + Dor no Corpo
Chinkungunya: Febre Alta + Manchas na pele'''

print('Digite 1 - sim ou 2 - não!')
febre = int(input('Você está com Febre Alta? \n'))
dor = int(input('Você está com Dor no corpo? \n'))
manchas = int(input('Você está com Manchas na pele? \n'))

if febre == 1 and dor == 1 and manchas == 2:
    print('Você está está com Dengue, procure um médico!')
elif febre == 1 and dor == 2 and manchas == 1:
    print('Você está com Chinkungunya, procure um médico!')
elif febre == 2 and dor == 1 and manchas == 1:
    print('Você está com Zika, procure um médico!')
elif febre == 1 and dor == 1 and manchas == 1:
    print('Você está com todos os sintomas, procure um médico o mais rápido possível!')
else:
    print('Você está bem!')