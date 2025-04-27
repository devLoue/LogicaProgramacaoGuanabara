#Exercício Python 012: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco = float(input('Digite o valor de um produto em R$:'))
print(f'O valor do produto com desconto de 5% é R${preco-(preco*0.05):.2f}')