# Peça para o usuário digitar o preço e quantidade de um produto.
# Numa loja é dado 10% de desconto quando o cliente compra 5 unidade ou mais do mesmo produto. Mostre qual é o valor o cliente
# paragará por esta compra.

preco = float(input('Digite o preço do produto: \n'))
qtd = int(input('Digite a quantidade do produto: \n'))
total = preco * qtd

if qtd >= 5:
    desconto = total - (total * 0.10)
    print('O valor total do produto com desconto é {}!'.format(desconto))
elif qtd < 5:
    print('O valor total do produto é {}'.format(total))
