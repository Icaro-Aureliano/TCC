from flask import Flask, render_template, request, redirect, session, url_for, send_from_directory
from dao import ClienteDao
from flask_mysqldb import MySQL
from modelo import Cliente
import os, time

app = Flask(__name__)
app.secret_key = 'teste'

app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = ""
app.config['MYSQL_DB'] = "Air_Control"
app.config['MYSQL_PORT'] = 3306
app.config['UP_CONFIG'] = os.path.dirname(os.path.abspath(__file__)) + '/uploads'

db = MySQL(app)
cliente_dao = ClienteDao(db)

@app.route('/')
def index():
    nome = request.args.get('nome')
    return render_template('paginicial.html', pagina = "Pagina inicial", nome_cliente = nome or "")

@app.route('/faleconosco')
def faleconosco():
    return render_template('faleconosco.html', pagina="Fale conosco")

@app.route("/quemsomos")
def quemsomos():
    return render_template('quemsomos.html', pagina="Quem somos")

@app.route('/criar', methods=['POST',])
def criar():
    try:
        nome = checar_nome(request.form['nome'])
        email = checar_email(request.form['email'])
        telefone = checar_numero(request.form['telefone'])
        chave = checar_chave(request.form['chave'])
        cliente = Cliente(nome, email, telefone, chave)
        cliente = cliente_dao.salvar(cliente)

        imagem = request.files['imagem']
        uploads_path = app.config["UP_CONFIG"]
        imagem.save(f'{uploads_path}/foto{cliente.nome}.jpg')

        return redirect(url_for('index'))
    except:
        return redirect(url_for('index'))

@app.route("/atualizar", methods=["POST", ])
def atualizar():
    imagem = request.files['imagem']
    nome_cliente= session['logado']
    deleta_foto(nome_cliente)
    uploads_path = app.config["UP_CONFIG"]
    imagem.save(f'{uploads_path}/foto{nome_cliente}.jpg')


def deleta_foto(nome):
    arquivo = recupera_imagem(nome)
    os.remove(os.path.join(app.config['UP_CONFIG'], arquivo))


def recupera_imagem(nome):
    for nome_arquivo in os.listdir(app.config['UP_CONFIG']):
        if f'foto{nome}' in nome_arquivo:
            return nome_arquivo

@app.route('/autenticar', methods=['POST', ])
def autenticar():
    email = request.form['email']
    chave = request.form['chave']
    cliente = cliente_dao.buscar_registro(email, chave)
    if cliente:
        if cliente.codigo == request.form['chave']:
            session['logado'] = cliente.email
            nome_cliente = cliente.nome.title()
            return redirect(url_for('produto_comprado'))
    else:
        return redirect(url_for('index'))

@app.route("/paginainicial")
def produto_comprado():
    
    if 'logado' not in session or session['logado'] == None:
        return redirect(url_for("index"))
    else:
        base_busca = str(session['logado'])
        nome = cliente_dao.buscar_nome(base_busca)
        foto_cliente = f'foto{nome}.jpg'
        if foto_cliente == None:
            foto = 'foto_padrao.jpg'
        else:
            foto = foto_cliente
        return render_template("paginicialcomprado.html", pagina="Produto",  nome_usuario= nome, cliente_foto = foto, qrcode = 'QRcode_exemplo.png')

@app.route('/logout')
def logout():
    session['logado'] = None
    return redirect(url_for('index'))

@app.route('/uploads/<nome_arquivo>')
def imagem(nome_arquivo):
    return send_from_directory('uploads', nome_arquivo)


def checar_nome(nome):
    lista = ["@", "-", "_", ".", "#", "%", "*","&","!", "?",]
    for caracter in lista:
        busca_nome = nome.find(caracter)
        if not busca_nome == -1:
            raise
    else:
        return nome.title()

def checar_email(email):
    if not email.find("@") == -1 and not email.find(".") == -1:
        return email
    else:
        raise 

def checar_numero(string):#rever
    parentese_01 = string.find("(")
    parentese_02 = string.find(")")
    if parentese_01 != -1 and parentese_02 != -1:
        ddd = string[parentese_01 + 1:parentese_02]
        if int(ddd) or len(ddd) > 2:
            return string
    else:
        return redirect(url_for('cadastro'))

def checar_chave(chave):
    resultado = cliente_dao.buscar_chave(chave)
    if resultado:
        raise
    else:
        return chave

@app.route("/downlaod")
def downloads():
    return redirect(url_for("'downloads', filename='aplicativo.txt'"))

app.run(debug=True)