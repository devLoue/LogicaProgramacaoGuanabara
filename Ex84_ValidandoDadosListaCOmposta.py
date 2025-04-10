#Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
#A) Quantas pessoas foram cadastradas.
#B) Uma listagem com as pessoas mais pesadas.
#C) Uma listagem com as pessoas mais leves.

listatemporaria = [] #Declarando uma lista "temporária"
listafinal = [] #Declarando minha lista "Final"
validador = " " #Validador com inicio vazio porém já declarado entre aspas pois vai receber um valor de string, "Deseja continuar S/N?"
maiorpeso = 0 #Lista de pessoas mais pesadas 
menorpeso = 0

while True:
    listatemporaria.append(str(input('Qual é o seu nome? ')))
    listatemporaria.append(float(input(f'Qual é o seu peso (em kg), {listatemporaria[0]}? ')))
    listafinal.append(listatemporaria[:])
    if maiorpeso == 0:
        maiorpeso = listatemporaria[1]
        menorpeso = listatemporaria[1]
    else:
        if listatemporaria[1] > maiorpeso:
            maiorpeso = listatemporaria[1]
        if listatemporaria[1] < menorpeso:
            menorpeso = listatemporaria[1]
    listatemporaria.clear()
    validador = str(input('Deseja cadastrar outra pessoa? S/N ')).strip().upper()
    while validador not in "SsNn":
        validador = str(input('Opção inválida. \nDeseja cadastrar outra pessoa? S/N ')).strip().upper()
    if validador in "N":
        break
    if validador in "S":
        continue
print(f'Cadastros feitos: {len(listafinal)}')
print(f'O maior peso foi de {maiorpeso}kg. peso de ', end ='')
for p in listafinal:
    if p[1] == maiorpeso:
        print(f'{p[0]} ', end ="")
print(f'\nO menor peso foi de {menorpeso}kg peso de ', end='')
for i in listafinal:
    if i[1] == menorpeso:
        print(f'{i[0]} ', end ="")