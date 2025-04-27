# Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
#[ 1 ] somar
#[ 2 ] multiplicar
#[ 3 ] maior
#[ 4 ] novos números
#[ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

n1 = float(input('Digite o primeiro valor: \n'))
n2 = float(input('Digite o segundo valor: \n'))
escolha = int(input('O que você deseja fazer? \n[1] SOMA \n[2] Multiplicação \n[3]Maior \n[4] Inserir novos números \n[5]Sair do programa \n'))
if escolha != 1 or 2 or 3 or 4 or 5:
    print('Digite uma opção válida! \n')
    escolha = int(input('O que você deseja fazer? \n[1] SOMA \n[2] Multiplicação \n[3]Maior \n[4] Inserir novos números \n[5]Sair do programa \n'))
while escolha != 1 or 2 or 3 or 4 or 5:
    if escolha == 1:
        print ('Você escolheu: SOMA \n{:.2f} + {:.2f} = {:.2f}'.format(n1,n2,n1+n2))
        escolha = int(input('O que você deseja fazer? \n[1] SOMA \n[2] Multiplicação \n[3]Maior \n[4] Inserir novos números \n[5]Sair do programa \n'))
    if escolha == 2:
        print ('Você escolheu: MULTIPLICAÇÃO \n{:.2f} * {:.2f} = {:.2f}'.format(n1,n2,n1*n2))
        escolha = int(input('O que você deseja fazer? \n[1] SOMA \n[2] Multiplicação \n[3]Maior \n[4] Inserir novos números \n[5]Sair do programa \n'))
    if escolha == 3:
        print('Você escolheu o número maior! \n')
        if n1 > n2:
            print ('O número maior entre {:.2f} e {:.2f} é {:.2f}'.format(n1,n2,n1))
            escolha = int(input('O que você deseja fazer? \n[1] SOMA \n[2] Multiplicação \n[3]Maior \n[4] Inserir novos números \n[5]Sair do programa \n'))
        if n2 > n1:
            print ('O número maior entre {:.2f} e {:.2f} é {:.2f}'.format(n1,n2,n2))
            escolha = int(input('O que você deseja fazer? \n[1] SOMA \n[2] Multiplicação \n[3]Maior \n[4] Inserir novos números \n[5]Sair do programa \n'))
        elif n1 == n2:
            print ('Os valores são iguais! \n')
    if escolha == 4:
        n1 = float(input('Digite o primeiro valor: \n'))
        n2 = float(input('Digite o segundo valor: \n'))
        escolha = int(input('O que você deseja fazer com os novos números? \n[1] SOMA \n[2] Multiplicação \n[3]Maior \n[4] Inserir novos números \n[5]Sair do programa \n'))
    if escolha == 5:
        print('O programa está sendo encerrado...')
        break