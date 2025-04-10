#Exercício Python 063: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. 
quantidadetermos = int(input('Quantos termos você quer? \n'))
termo1 = 0
termo2 = 1
contador = 3
print ("{} - {}".format(termo1, termo2), end='')
while contador <= quantidadetermos:
    termo3 = termo1 + termo2
    print(' - {}'.format(termo3), end='')
    termo1 = termo2
    termo2 = termo3
    contador = contador +1