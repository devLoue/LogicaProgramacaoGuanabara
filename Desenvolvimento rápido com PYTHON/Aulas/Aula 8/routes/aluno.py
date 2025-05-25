from flask import Blueprint
from database import alunos

aluno_route= Blueprint('aluno', __name__)

@aluno_route.route('/')
def lista_alunos():
    return alunos;

@aluno_route.route('/', methods=['POST'])
def inserir_aluno():
    pass


@aluno_route.route('/new')
def form_aluno():
    pass


@aluno_route.route('/<int:aluno_id>')
def obter_aluno(aluno_id):
    pass
