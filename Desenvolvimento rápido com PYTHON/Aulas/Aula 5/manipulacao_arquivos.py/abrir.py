# open open(“arquivo.txt”), para os casos em que o arquivo está no mesmo diretório do script.
#open(“../arquivo.txt”), para os casos em que o arquivo está no diretório acima do script.

arquivo = open("arquivo.txt") ##método padrão r(read), modo de leitura.
for palavra in arquivo: #para cada palavra dentro do arquivo 
    print(palavra)




    
arquivo.close
