# Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.
listadeprecos = ('Lápis', 2, 'Caneta', 2.5, 'Caderno', 30, 'Borracha', 5, 'Régua', 30)
for posicao in range (0, len(listadeprecos)):
    if posicao % 2 == 0:
        print(f'{listadeprecos[posicao]:.<30}', end = ' ')
    if posicao % 2 == 1:
        print(f'R$ {listadeprecos[posicao]:>4.2f}')