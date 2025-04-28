#Criando um dicionário para armazenar os dados de uma pessoa que iremos chamar de pessoa1
pessoa1 = {"nome": "Luiz", "idade" : 26, "email": "luiz@email.com"}

#Exibindo na tela o dicionário inteiro de pessoa
print(f"Pessoa 1: {pessoa1}")

#Exibindo apenas uma chave do dicionário pessoa, no caso o nome
print(pessoa1["nome"])

#Exibindo apenas uma chave (email)
print(pessoa1["email"])

#Criando pessoa2
pessoa2= {"nome":"Maisa", "idade": 56, "email" : "maisa@email.com"}

#Exibindo pessoa 2
print(f"Pessoa 2: {pessoa2}")

#Colocando pessoa 1 e pessoa 2 dentro de um outro dicionário chamado PESSOAS, ou seja, um dicionário para armazenar dados de diversas pessoas
pessoas = {"Pessoa1": pessoa1, "Pessoa2": pessoa2}
print(pessoas)

#Acessando apenas o nome da Pessoa 2 que está dentro de pessoas
print(pessoas["Pessoa2"]["nome"])