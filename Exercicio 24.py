''' Peça para o usuário digitar sua preferencia: Marvel ou DC. Se ele escolher Marvel, peça para ele escolher
entre Capitão América ou Homem dde Ferro. Se ele escolher DC, peça para ele escolher entre o Batman ou Superman.
Mostre qual foi o super herói que ele escolheu'''

print('Você prefere Marvel ou DC?')
prefe = int(input('1 - Marvel ou 2 - DC! \n'))
if prefe == 1:
    print('Você prefere o Capitão América ou o Homem de Ferro?')
    marvel = int(input('1 - Capitão América ou 2 - Homem de Ferro! \n'))
    if marvel == 1:
        print('O Herói escolhido foi o Capitão América!')
    elif marvel == 2:
        print('O Herói escolhido foi o Homem de Ferro! \n')
    else:
        print('Opção Invalída!')
elif prefe == 2:
    print('Você prefere o Superman ou o Batman?')
    DC = int(input('1 - Superman ou 2 - Batman! \n'))
    if DC == 1:
        print('O Herói escolhido foi o Superman!')
    elif DC == 2:
        print('O Herói escolhido foi o Batman!')
    else: 
        print('Opção Invalída!')
else:
    print('Opção Invalída!')