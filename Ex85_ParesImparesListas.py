#Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
#No final, mostre os valores pares e ímpares em ordem crescente.


#Solucao 1: 
"""inteiros = []
temporaria = []
pares = []
impares = []

for i in range (1, 8):
    temporaria.append(int(input('Digite um número inteiro:')))
for valor in temporaria:
    if valor % 2 ==0:
        pares.append(valor)
    elif valor % 2 ==1:
        impares.append(valor)
inteiros.append(impares)
inteiros.append(pares)
impares.sort()
pares.sort()
print(f'Números digitados: {temporaria} \nImpares em ordem crescente: {impares} \nPares em ordem crescente {pares}')"""

# Solução2 (MAIS OTIMIZADA)

inteiros = [[], []]
valortemporario = 0
for i in range (0, 7):
    valortemporario=int(input('Digite um número inteiro:'))
    if valortemporario % 2 == 0:
        inteiros[0].append(valortemporario)
    elif valortemporario % 2 ==1:
        inteiros[1].append(valortemporario)
print(f'Todos os valores: {inteiros}')
for pos, valor in enumerate(inteiros):
    inteiros[pos].sort()
print(f'Pares em ordem crescente: {inteiros[0]} \nImpares em ordem crescente{inteiros[1]}')