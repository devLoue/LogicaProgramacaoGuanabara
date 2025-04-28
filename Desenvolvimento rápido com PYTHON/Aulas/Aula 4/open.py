arquivo = open("arquivo.txt", "r") #Abrindo o arquivo "meu_arquivo.txt" e o atribuindo á uma variavel chamada arquivo
print (arquivo)
print(f"Nome do arquivo: {arquivo.name}") #Exibindo nome do arquivo
print(f"Modo do arquivo: {arquivo.mode}") #Exibindo o modo, se é leitura, se é escrita...
print(f'O arquivo foi fechado? {arquivo.closed}') #a função .closed é um booleano que retornará false caso o arquivo esteja aberto e true caso esteja fechado
print(f"Exibindo o conteúdo do arquivo txt: {arquivo.read()}")
print("Fechando arquivo...")
arquivo.close()
print(f'O arquivo foi fechado? {arquivo.closed}') #Retornando true, já que fechamos na linha acima

