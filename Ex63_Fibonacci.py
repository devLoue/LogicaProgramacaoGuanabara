#Exercício Python 063: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. 
quantidadetermos = int(input('Quantos termos você quer? \n'))
t1 = 0
t2 = 1
contador = 3
print ("{} - {}".format(t1, t2), end='')
while contador <= quantidadetermos:
    t3 = t1 + t2
    print(' - {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    contador = contador +1