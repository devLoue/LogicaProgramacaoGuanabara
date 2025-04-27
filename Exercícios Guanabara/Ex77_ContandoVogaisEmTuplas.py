listadepalavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')
for palavra in listadepalavras:
    print(f'\nNa palavra {palavra} temos:', end = ' ')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print (letra, end = ' ')