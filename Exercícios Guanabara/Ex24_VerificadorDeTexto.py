#Exercício Python 024: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".
cidade = str(input('Digite o nome da cidade em que você nasceu: \n')).strip().upper()
nomes_separados= cidade.split()
if 'SANTO' == nomes_separados[0]:
    print(f'Santo é o primeiro nome da sua cidade. \nNome da sua cidade: {cidade.title()}')
if 'SANTO' not in nomes_separados[0]:
    print(f'Santo não é o primeiro nome da sua cidade. \nNome da sua cidade: {cidade}')