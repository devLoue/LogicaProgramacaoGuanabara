expressao = str(input('Digite a expressão desejada:'))
lista = []
for char in expressao: #para cada caracter digitado na expressão
    if char == '(': #se o caracter for igual ao ( parênteses abrindo
        lista.append('(') #coloque-o na lista, coloque o parentêses aberto na lista
    elif char == ')': #se não, se nao for um parenteses abrindo e sim um fechando, então...
        if len(lista) > 0: #se a lista estiver vazia... = tamanho dela for igual a 0
            lista.pop()#remove o último item da lista
        else: # se nao, se a lista estiver cheia
            lista.append(')') # coloque um parenteses fechando, par do parenteses abrindo encontrando seu par
            break #quebre o laço
if len(lista) == 0: 
    print('Sua expressão está válida')
else: 
    print('Sua expressão está inválida')