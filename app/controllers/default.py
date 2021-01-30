from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/atividade1')
def atividade1():
    return render_template('atividade1.html')


@app.route('/atividade2-WR')
def reading_and_writing():
    return render_template('requisitionsWR.html')

@app.route('/atividade2-load')
def load():
    return render_template('requisitionsL.html')


@app.route('/atividade2-conteudo')
def conteudo():
    return render_template('content.html')

