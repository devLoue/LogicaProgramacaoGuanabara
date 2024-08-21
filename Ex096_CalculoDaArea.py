#Exercício Python 096: Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.
def area(largura, altura):
    r = largura * altura
    print(f'A área de altura {altura}m e com largura de {largura}m, possui {r} m2 de área')


altura = float(input('Digite a altura em metros: '))
largura = float(input('Digite a largura em metros :'))
area(altura, largura)
