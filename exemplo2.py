#Algoritmo "exercicio62"
#// Elabore um programa que tenha declarado 2 vetores,
#//sendo um para armazenar uma sequencia de caracteres
#//e outro de números reais. Peça para o usuário
#//digitar o nome e a nota de 20 alunos e guarde estas
#//informações nos 2 vetores. Pergunte para o usuário
#//se ele deseja visualizar a lista de alunos aprovados
#//(nota >=6) ou reprovados (nota < 6) e exiba o nome
#//dos alunos de acordo com a escolha do usuário.

#"declara" variáveis
nomes = []
notas = []
opcao = 0

def aprovados():
    #lista dos aprovados
    for i in range(0,len(notas)):
        if (notas[i] >= 6):
            print(nomes[i], " - ", notas[i])
 

def reprovados():
    #lista dos reprovados
    for i in range(0, len(notas)):
        if (notas[i] < 6):
            print(nomes[i], " - ", notas[i])

def digitar():
    #adiciona uma 
    posicao = len(notas)
    nomes.append("")
    notas.append(0)
   
   
    print("Digite o nome do ", posicao, "° aluno")
    nomes[posicao] = input()

    print("Digite a nota do ", nomes[posicao])
    notas[posicao] = float(input())

   
def mostrarmedia():
    total = 0
    for i in range(0,len(notas)):
        total = total + notas[i]
    
    media = total / len(notas)
    print("Média das notas: ", media)
       

while (opcao != 5):
    print("Qual opção deseja? ")
    print("1 - adicionar aluno")
    print("2 - consultar alunos aprovados")
    print("3 - consultar alunos reprovados")
    print("4 - mostrar média das notas")
    print("5 - sair")
    opcao = int(input())

    if (opcao == 1):
        digitar()
    elif (opcao == 2):
        aprovados()
    elif (opcao == 3):
        reprovados()
    elif (opcao == 4):
        mostrarmedia()
    else:
        print("opcao inválida")
