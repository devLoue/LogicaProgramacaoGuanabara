# Exercício Python 056: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

somaidade = 0
mediaidade = 0
mulheres20 = 0
maioridadehomem = 0
nomedomaisvelho = ''
for i in range (1,5):
    nome = str(input('Digite seu nome: \n')).strip()
    idade = int(input('Digite sua idade: \n'))
    sexo = str(input('Sexo: M/F? : \n'))
    somaidade = somaidade + idade
    if i == 1 and sexo in 'Mm':
        if sexo in 'Mm' and idade > maioridadehomem:
            maioridadehomem = idade
            nomedomaisvelho = nome
    if i == 1 and sexo in 'Ff' and idade < 20:
        mulheres20 = mulheres20 + 1
    if i == 2 and sexo in "Mm":
        if sexo in 'Mm' and idade > maioridadehomem:
            maioridadehomem = idade
            nomedomaisvelho = nome
    if i == 2 and sexo in 'Ff' and idade <20:
        mulheres20 = mulheres20 + 1
    if i == 3 and sexo in 'Mm':
        if idade > maioridadehomem and sexo in 'Mm':
            maioridadehomem = idade
            nomedomaisvelho = nome
    if i == 3 and sexo in 'Ff' and idade <20:
        mulheres20 = mulheres20 + 1
    if i == 4 and sexo in 'Mm':
        if idade > maioridadehomem and sexo in 'Mm':
            maioridadehomem = idade
            nomedomaisvelho = nome
    if i == 3 and sexo in 'Ff' and idade <20:
        mulheres20 = mulheres20 + 1
mediaidade = somaidade / 4
print ('A média de idade do grupo é de {} anos'.format(mediaidade))
print ('O homem mais velho tem {} anos e seu nome é {}'.format(maioridadehomem, nomedomaisvelho))
print ('A quantidade de mulheres que tem menos de 20 anos é {}'.format(mulheres20))