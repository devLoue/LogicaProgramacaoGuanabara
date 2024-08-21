# Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
#OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

#inicio do programa + minha resolucao (errada, bug em grandes valores)
"""print('Banco dos ex rico, entra pobre e sai fudido')

notade50 = 0
notade20 = 0
notade10 = 0
notade1 = 0
resto= 0
resto1= 0
resto2= 0
valordosaque = int(input('Qual valor você quer sacar? R$'))

#validacoes
if valordosaque >= 50:
    notade50 = valordosaque // 50
    resto = valordosaque - (50*notade50)
    if resto >= 20: 
        notade20 = resto // 20
        resto1 = resto - (notade20*20)
        print('resto de 20', resto1)
        if resto1 >= 10:
            notade10 = resto1 // 10
            resto2 = resto1 -(notade10*10)
            if resto2 <= 9:
                notade1 = resto2 // 1
print(f'Total de {notade50} cédulas de R$ 50')
print(f'Total de {notade20} cédulas de R$ 20')
print(f'Total de {notade10} cédulas de R$ 10')
print(f'Total de {notade1} cédulas de R$ 1') """

# inicio com while

print ('Banco dos bugados')
total = int(input('Quanto você deseja sacar?'))
ced = 50
totalced50 = 0
totalced20 = 0
totalced10 = 0
totalced1 = 0
while True:
    if total >= ced:
        total = total - ced
        totalced50 = totalced50 + 1
    else:
        if ced == 50:
            ced = 20
        if total >= ced:
            total = total - ced
            totalced20 = totalced20 + 1
        else:
            if total < ced:
                 ced = 10
                 while total >= ced:
                      total = total - ced
                      totalced10 = totalced10 + 1
                      if total < ced and total > 1:
                           ced = 1 
                           while total >= ced:
                                total = total - ced
                                totalced1 = totalced1 + 1
    if total == 0:
        break
print(f'Total de {totalced50} cédulas de R$ 50')
print(f'Total de {totalced20} cédulas de R$ 20')
print(f'Total de {totalced10} cédulas de R$ 10')
print(f'Total de {totalced1} cédulas de R$ 1') 