from flask import render_template,request
from app import app
from ..models import usuario_teste

mensage_teste = ""

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
def load():
    return render_template('requisitionsL.html')


@app.route('/atividade2-conteudo')
def conteudo():
    return render_template('content.html')


