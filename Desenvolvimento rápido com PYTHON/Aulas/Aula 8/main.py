from flask import Flask 

#Inicializando 
app = Flask(__name__)

#rota home
@app.route("/")
def ola_mundo():
    return "Hello world"

app.run(debug=True) #execução e ativa o "Modo desenvolvedor, vai auxiliar enquanto estiver desenvolvendo"


