#Exercício Python 033: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

maior=0
menor=0

for i in range (1, 4):
    n = int(input(f'Digite o {i} número:'))
    if maior == 0 and menor == 0:
        maior = n
        menor = n
    if n > maior:
        maior = n
    if n < menor:
        menor = n
print(f'O maior número digitado foi {maior}')
print(f'O menor número digitado foi {menor}')