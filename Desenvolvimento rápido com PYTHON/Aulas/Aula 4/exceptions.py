try:
    with open('meu_arquivo.txt', 'w') as file:
        file.write('Este é o novo conteúdo.')
        print(file)
except FileNotFoundError:
    print("Erro ao abrir o arquivo.")