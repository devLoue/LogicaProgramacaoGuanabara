# Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.
listanum = []
listapar = []
listaimpar = []

while True:
    listanum.append(int(input('Digite um valor a ser inserido na lista:')))
    decisao = str(input('Deseja continuar [S/N]?')).strip().upper()[0]
    while decisao not in 'SN':
        decisao = str(input('Deseja continuar [S/N]?')).strip().upper()[0]
    if decisao in 'N':
        break
print(f'Você digitou os seguintes valores: {listanum}')
for numero in listanum:
    if numero % 2 == 0:
        listapar.append(numero)
    if numero % 2 == 1:
        listaimpar.append(numero)
print(f'Números impar da lista: {listaimpar}')
print(f'Números pares da lista: {listapar}')