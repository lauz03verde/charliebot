import requests
import json

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['POST'])
def main():
    data = request.get_json(silent=True)
    
    intentName = data['queryResult']['intent']['displayName']
    nome = data['queryResult']['parameters']['nome']
    cpf = data['queryResult']['parameters']['cpf']
    telefone = data['queryResult']['parameters']['telefone']
    
    if intentName == "2 - quero checar minha mensalidade":
        data['fulfillmentText'] = f"Pesquisando o CPF: {cpf}..."
        
    return jsonify(data)

if __name__ == "__main__":
    app.debug = False
    app.run()