from flask import render_template,request,jsonify,make_response,Flask
import jwt
import datetime
from app import app
from functools import  wraps
from ..models import usuario_teste

def token_validation(f):
    @wraps(f)
    def decorated(*args,**kwargs):
        token = request.args.get('token')

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
def atividade1():
    return render_template('atividade1.html')


@app.route('/atividade2-WR',methods=['POST', 'GET'])
def reading_and_writing():


    if request.method == 'GET':
        return render_template('requisitionsWR.html')

    elif request.method == 'POST':
        text_test = request.form.get('texto')

        return '<h1>O texto {} foi enviado'.format(text_test)



@app.route('/mensages',methods=['GET'])
def mensages():
    return usuario_teste.paulo




@app.route('/atividade2-load')
@token_validation
def load():
    return render_template('requisitionsL.html')


@app.route('/atividade2-conteudo')
def conteudo():
    return render_template('content.html')

@app.route('/pagina-login')
def login():
    auth = request.authorization

    if auth and auth.password == 'password' and auth.username =='paulo':
        token = jwt.encode({'user' : auth.username, 'exp':datetime.datetime.utcnow()+datetime.timedelta(seconds=5)},app.config['SECRET_KEY'])

        return jsonify({'token': token.decode('UTF-8')})

    return make_response('teste',401,{'WWW-Authenticate':'Basic realm="Login Required"'})






@app.route('/pagina-protegida')
@token_validation
def pagina_protegida():
    return render_template('pagina-protegida.html')



