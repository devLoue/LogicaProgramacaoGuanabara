#Exercício Python 025: Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome = str(input('Digite o seu nome: \n')).strip()
print ('Seu nome tem silva? {}'.format('SILVA' in nome.upper()))
