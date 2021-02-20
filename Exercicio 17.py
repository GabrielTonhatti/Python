# Exercicio 17
# peça para o usuário digitar o nome e a idade de duas pessoas.
# Mostre o nome da pessoa mais nova.

nome = input('Digite o 1º nome: \n')
idade = int(input('Digite a idade do(a) {}\n'.format(nome)))
nome2 = input('Digite o 2º nome: \n')
idade2 = int(input('Digite a idade do(a) {}\n'.format(nome2)))

if idade > idade2:
    print('A pessoa mais nova é {}'.format(nome2))
else:
     print('A pessoa mais nova é {}'.format(nome))

