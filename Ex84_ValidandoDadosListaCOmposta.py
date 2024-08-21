#Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
#A) Quantas pessoas foram cadastradas.
#B) Uma listagem com as pessoas mais pesadas.
#C) Uma listagem com as pessoas mais leves.

listatemp = []
ppesadas = []
pleves = []
listaprincipal = []
totaldepessoas = 0
#Iniciando o programa:
while True:
    listatemp.append(str(input('Digite o nome: ')))
    listatemp.append(float(input('Digite o seu peso: ')))
    totaldepessoas = totaldepessoas + 1

    #Adicionando o primeiro valor na lista de leves e de pesados:
    if len(ppesadas) == 0:
        ppesadas.append(listatemp[:])
    if len(pleves) == 0:
        pleves.append(listatemp[:])
    # Adicionando cada valor a lista principal e depois limpando a temporária...
    listaprincipal.append(listatemp[:])
    listatemp.clear()

    #Decisao se deseja cadastrar mais pessoas
    decisao = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    while decisao not in 'SN':
        decisao = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if decisao == 'N':
        break

#Verificando os maiores valores da lista de pesados
listaprincipal.pop(0)
for pos, elemento in enumerate(listaprincipal):
    if pos % 2 == 1:
        if pos >= ppesadas[0][1]:
            print(f'posição {pos} elemento {elemento}')
            ppesadas.append(listaprincipal[pos])

print('lista principal ',listaprincipal)
print('lista dos pesados: ', ppesadas)
print(f'Foram cadastradas {totaldepessoas} pessoas.')
print(f'A pessoa mais pesada é {ppesadas[0][0]} com {ppesadas[0][1]} kg')
print(f'A pessoa mais leve é {pleves[0][0]} com {pleves[0][1]} kg')