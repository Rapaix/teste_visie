from flask import Flask, render_template, request, redirect
from app.database import connection, save_pessoas,delete_pessoas, select_pessoas

app = Flask(__name__)
app.config['SECRET_KEY'] = 'testevisie'


@app.route("/", methods=['GET'])
def index():
    lista = select_pessoas()
    print(lista)
    return render_template("index.html", lista= lista)

@app.route("/teste")
def home():
    return "Teste"

@app.route("/save", methods=['POST'])
def save():
  dados_registro = {
    "nome": request.form['nome'],
    "rg": request.form['rg'],
    "cpf": request.form['cpf'],
    "data_nasc": request.form['data_nasc'],
    "data": request.form['data'],
    "funcao": request.form['funcao']
  }  
  save_pessoas(dados_registro)
  return redirect('/')

@app.route("/delete/<id_pessoa>", methods=['GET'])
def delete(id_pessoa):
  print(id_pessoa)
  delete_pessoas(id_pessoa)
  return redirect('/')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
