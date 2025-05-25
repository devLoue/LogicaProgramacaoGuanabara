# open open(“arquivo.txt”), para os casos em que o arquivo está no mesmo diretório do script.
#open(“../arquivo.txt”), para os casos em que o arquivo está no diretório acima do script.

arquivo = open("arquivo.txt") ##método padrão r(read), modo de leitura.
conteudo = arquivo.readlines()
print("type arquivo:",type(arquivo))
print("type conteudo: ",type(conteudo)) ##conteudo = arquivo.readlines() é uma lista
print("arquivo.nome: ",arquivo.name)
print("arquivo.mode: ",arquivo.mode)
print("arquivo.closed: ",arquivo.closed)#False antes do arquivo.close()
print("arquivo.closed: ",arquivo.closed)##True após o arquivo.close()

for linha in arquivo:
    print(linha)


"""print(arquivo.read()) #Retorna todo o conteúdo de um arquivo como uma única string.
print(arquivo.readline()) #Retorna uma linha de arquivo, incluindo caracteres de final (\n ou \r\n), e avança o cursor para a próxima.
print(arquivo.readlines()) #Retorna uma lista em que cada item da lista é uma linha do arquivo"""
