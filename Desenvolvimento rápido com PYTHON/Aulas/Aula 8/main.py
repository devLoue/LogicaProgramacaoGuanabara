from flask import Flask 
from routes.home import home_route  #routes.home pasta routes arquivo home, "home.py" importando a variável de contexto home_route
from routes.aluno import aluno_route
#Inicializando 
app = Flask(__name__)

app.register_blueprint(home_route)
app.register_blueprint(aluno_route,url_prefix='/alunos')

app.run(debug=True) #execução e ativa o "Modo desenvolvedor, vai auxiliar enquanto estiver desenvolvendo"


