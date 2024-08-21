# Exercício Python 022: Crie um programa que leia o nome completo de uma pessoa e mostre: 
# - O nome com todas as letras maiúsculas e minúsculas.
# - Quantas letras ao todo (sem considerar espaços).
# - Quantas letras tem o primeiro nome. 


name = str(input("Digite o seu nome: \n")).strip() #Solicitando nome do usuário

print('Estou pensando...') #Apenas um texto para tentar quebrar o "gelo de máquina" 
print(f'O seu nome todo em minúsculo é: {name.lower()}') #Mostrando na tela do usuário o retorno do nome dele + a chamada da função lower() que deixa tudo minúsculo
print(f'O seu nome todo em maiúsculo é: {name.upper()}') #Mostrando na tela do usuário o retorno do nome dele + a chamada da função upper() que deixa tudo maiúsculo
print(f'O seu nome tem {len(name) - (name.count(" "))} letras') #Aqui vem a primeira expressão (tamanho do nome - os espaços digitados pelo usuário)
array = name.split() #Função split() divide todas as palavras separadas por espaço em uma lista e os agrupa em um único objeto(variável)
print(f'O seu primeiro nome tem {len(array[0])} letras') #Mostrando na tela do usuário o retorno do primeiro nome dele + a chamada da função upper() que deixa tudo em maiúsculo


