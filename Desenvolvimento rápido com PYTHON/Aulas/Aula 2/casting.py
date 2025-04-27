
## O input por padrão armazena uma string
numero1 = input("Digite um numero: ")
print(numero1)
print(type(numero1)) #mostrando que armazenamos um número digitado porém como string

## Armazenando a segunda string contendo um número também
numero2 = input("Digite um outro numero: ")
print(numero2)

##Fazendo o casting das duas strings para inteiro
soma = int(numero1) + int(numero2)
print("A SOMA DOS NUMEROS SAO: ", soma)