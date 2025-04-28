try:
    with open('meu_arquivo.txt', 'w') as file:
        file.write('Este é o novo conteúdo.')
except FileNotFoundError:
    print("Erro ao abrir o arquivo.")