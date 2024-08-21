# Exercício Python 030: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

n = int(input("Me diga um número e eu te digo se ele é par ou impar \nNúmero: "))
if n % 2 == 0:
    print(f'{n} é par')
elif n % 2 != 0:
    print(f'{n} é impar')