
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def inicio():
    return jsonify({
        "mensagem": "Bem-vindo à DevFlow Solutions!",
        "status": "Aplicação funcionando"
    })

@app.route("/produtos")
def produtos():
    return jsonify([
        {"id": 1, "nome": "Camiseta", "preco": 59.90},
        {"id": 2, "nome": "Tênis", "preco": 199.90}
    ])

if __name__ == "__main__":
    app.run()
