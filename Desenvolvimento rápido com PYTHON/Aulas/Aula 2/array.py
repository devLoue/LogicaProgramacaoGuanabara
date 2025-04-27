vetores_de_dados = [1, 4, 4, 8, 9, 21, 2] #Declarando um vetor/array em python

#Fazendo um for que percorre todo o array 
for dado in vetores_de_dados:
    #Se o dado dentro do array for igual a 8, o algoritimo irá exibir o próprio dado, ou seja, 8. Caso não tenha nenhum valor 8, nada acontece...
    if dado == 8:    
        print(dado) #Imprimindo 8 na tela...
print("Encerrando o primeiro for...")

#A função len mostra o tamanho do vetor, ou melhor, quantos elementos este vetor possui, neste exemplo acima vetores_de_dados possuem 7 elementos.
for dado in range(len(vetores_de_dados)): #Neste exemplo, dado começa com o valor 0, e vai de 0 até 7 (tamanho ou len de vetores_de_dados)
    print(vetores_de_dados[dado])
print("Encerrando o segundo for...")


for dado in range(len(vetores_de_dados)):
    print(dado) #indo de 0 até 7, porém,
    ##Quando o dado tiver o valor 5, ou seja, quando o dado ir do 0 ao 5
    if dado == 5:
        print(vetores_de_dados[dado])#exiba na tela o valor da posição 5 do vetor, no caso o 21, lembrando que o indice de vetores começa em 0 logo o [5] possui valor 21 e não 9
print("Encerrando o terceiro for...")