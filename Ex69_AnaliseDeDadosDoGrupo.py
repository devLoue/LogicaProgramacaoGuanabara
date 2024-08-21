# Exercício Python 069: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
#A) quantas pessoas tem mais de 18 anos.
#B) quantos homens foram cadastrados.
#C) quantas mulheres tem menos de 20 anos. 

maiores18 = 0
numerodehomens = 0
mulheresmenoresde20 = 0

#Inicio
print('Cadastro de pessoas.')
while True:
    idade = int(input('Idade?'))
    sexo = str(input('Masculino ou feminino? [M/F]')).strip().upper()[0]
    # Validação se o sexo é masculino ou feminino...
    while sexo not in 'MmFf':
        print ('Sexo inválido')
        sexo = str(input('Masculino ou feminino? [M/F]')).strip().upper()[0]
    #inicio das somas
    if sexo == 'M' or sexo == 'F':
        if idade >= 18:
            maiores18 = maiores18 + 1
        if sexo == 'M':
            numerodehomens = numerodehomens + 1
        if sexo == 'F' and idade <=20:
            mulheresmenoresde20 = mulheresmenoresde20 + 1  
    decisao = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    while decisao not in 'SsNn':
        print('Opção inválida.')
        decisao = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if decisao in 'Nn':
        break
    if decisao in 'Ss':
        print('Cadastro de pessoas.')
print (f'Número de pessoas de 18 anos ou maiores: {maiores18}')
print (f'Número de homens cadastrados: {numerodehomens}')
print (f'Número de mulheres de 20 anos ou menos: {mulheresmenoresde20}')