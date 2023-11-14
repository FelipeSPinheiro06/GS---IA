from flask import Flask, jsonify, request

#Criar a API
app = Flask(__name__)

#Criar a rota Home para teste
@app.route("/")

#Criando a função para retornar uma mensagem
def home():
    return("A API está no ar")


if(__name__ == "__main__"):
    app.run(debug=True)
