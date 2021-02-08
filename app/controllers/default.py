from flask import render_template,request,jsonify,make_response,Flask,Response
import flask
import jwt
import datetime
from app import app
from functools import  wraps
from ..models import usuario_teste

def token_validation(f):
    @wraps(f)
    def decorated(*args,**kwargs):
        token = request.headers.get('Authorization')
        print(token)

        if not token:
            return ({'mensages': 'Sem token'}),403

        try:
            data = jwt.decode(token,app.config['SECRET_KEY'])
        except:
            return jsonify({'mensages': 'token nao correspondente ' }), 403

        return f(*args, **kwargs)

    return decorated




@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/atividade1')
@token_validation
def atividade1():
    return render_template('atividade1.html')


@app.route('/atividade2-WR',methods=['POST', 'GET'])
@token_validation
def reading_and_writing():


    if request.method == 'GET':
        return render_template('requisitionsWR.html')

    elif request.method == 'POST':
        text_test = request.form.get('texto')

        return '<h1>O texto {} foi enviado'.format(text_test)



@app.route('/mensages',methods=['GET'])
@token_validation
def mensages():
    return usuario_teste.paulo




@app.route('/atividade2-load')
@token_validation
def load():
    return render_template('requisitionsL.html')


@app.route('/atividade2-conteudo')
@token_validation
def conteudo():
    return render_template('content.html')

@app.route('/pagina-login',methods=['POST', 'GET'])
def autenticacao():
    if request.method == 'GET':
        return render_template('login-page.html')



@app.route('/login',methods=['POST','GET'])
def login():
    user = request.form.get('usuario')
    senha = request.form.get('senha')

    erro = None

    if  senha == '123' and user =='paulo':
        token = jwt.encode({'user' : user, 'exp':datetime.datetime.utcnow()+datetime.timedelta(seconds=5)},app.config['SECRET_KEY'])
        return render_template('pagina-protegida.html', token = token.decode('UTF-8'))

    else:
        erro = 'Usuário ou senho errados'
        return render_template('login-page.html',erro = erro)


@app.route('/pagina-protegida')
@token_validation
def pagina_protegida():
    return render_template('pagina-protegida.html')

@app.route('/teste')
@token_validation
def teste():
    return {'name' : 'paulo',
            'age': '21',
            'country': 'Brazil'}



