from flask import Flask

app = Flask(__name__)

@app.route("/olamundo/<usuario>/<int:idade>/<float:altura>")
def hello_world(usuario, idade, altura):
        return {
        "Usuário": usuario,
        "Idade": idade,
        "Altura": altura,
    }

@app.route("/bemvindo")
def bem_vindo():
        return {"message":"Olá mundo"}

@app.route("/bemvindo")
def projects():
        return "The project page"