# Reajuste salarial 
#Exercício Python 013: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Qual é o seu salário? '))
novosalario = salario + salario * 0.15
print(f'Salário anterior: R${salario:.2f}, novo salário R${novosalario:.2f}')