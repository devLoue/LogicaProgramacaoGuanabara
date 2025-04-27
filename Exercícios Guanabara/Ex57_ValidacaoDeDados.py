#Exercício Python 057: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.
sexo = str(input('Informe seu sexo [M/F] \n')).strip().upper()[0]
while sexo not in 'FM':
    print ('Dados inválidos, por favor, informe o seu sexo:')
    sexo = str(input('Informe o seu sexo [M/F] \n')).strip().upper()[0]
    if sexo in 'MF':
        print ('Sexo {} registrado com sucesso'.format(sexo))