#Exercício Python 020: O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle
list = []

for name in range (1, 5):
    list.append(input(f'Digite o {name} nome:'))
shuffle(list) #Embaralhando a lista, misturando...
print(f'A ordem de apresentação é {list}')