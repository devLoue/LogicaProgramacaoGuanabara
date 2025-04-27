principal = []
temporaria = []
maior = 0
menor = 0
totaldepessoas = 0
#iniciando o programa
while True:
    temporaria.append(str(input('Digite o nome: ')))
    temporaria.append(float(input('Digite o peso: ')))
    totaldepessoas = totaldepessoas + 1
    if len(principal) == 0:
        maior = menor = temporaria[1]
    if temporaria[1] > maior:
        maior = temporaria[1]
    if temporaria[1] < menor:
        menor =  temporaria [1]
    principal.append(temporaria[:])
    temporaria.clear()
#Decisao se deseja cadastrar mais pessoas
    decisao = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    while decisao not in 'SN':
        decisao = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if decisao == 'N':
        break
print(f'O maior peso foi {maior:.2f}kg peso de:')
for p in principal:
    if p[1] == maior:
        print(f'{p[0]} ')
print(f'O menor peso foi {menor:.2f}kg, peso de: ')
for p in principal:
     if p[1] == menor:
        print(f'{p[0]} ')
print('total de pessoas cadastradas: ', totaldepessoas)