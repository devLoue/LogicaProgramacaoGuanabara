# Exercício Python 070: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
#A) qual é o total gasto na compra.
#B) quantos produtos custam mais de R$1000.
#C) qual é o nome do produto mais barato. 

#iniciando as variavéis
total = 0
maiorde1000 = 0
produtomaisbarato = 100000
nomedoproduto = ' '
print('Loja super baratão')

#inicio do laço
while True:
    decisao = ' '
    produto = str(input('Qual é o nome do produto?'))
    preco = int(input('Preço: R$'))
    total = total + preco
    if preco >= 1000:
        maiorde1000 = maiorde1000 + 1
    if preco < produtomaisbarato:
        produtomaisbarato = preco
        nomedoproduto = produto
    while decisao not in 'SsNn': 
        decisao = str(input('Deseja cadastrar outro produto? [S/N]')).strip().upper()[0]         
    if decisao in 'Nn':
        print('Encerrando...')
        break
    if decisao in 'Ss':
        print('Proximo produto...')              
print(f'Total da compra: R$ {total:.2f}')
print(f'Total de produtos acima de R$ 1000.00: {maiorde1000}')
print(f'O produto mais barato é "{nomedoproduto}" e o seu valor é de R$ {produtomaisbarato:.2f}')