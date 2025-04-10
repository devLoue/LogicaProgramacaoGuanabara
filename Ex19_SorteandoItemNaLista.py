#Exercício Python 019: Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
#Utilizando a biblioteca random para números aleatórios, vamos utilizar a função choice (escolha)

from random import choice
list = ["PH", "Ebert", "Nelsin", "Caio", "V", "Guto", "Loue", "Kaua", "Julio"]
for name in range (1,5):
    ##list.append(input(f'Digite o {name} nome: '))
    print(f'O sorteado foi foi {choice(list)}')
print(list);

 