from flask import Flask, request, jsonify
import csv
import os

app = Flask(__name__)

# Verifica se o arquivo CSV já existe; caso contrário, cria o arquivo com cabeçalhos
csv_file = 'cadastro_alunos.csv'
if not os.path.exists(csv_file):
    with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Nome', 'Curso'])  # Cabeçalhos do arquivo CSV

@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    data = request.get_json()
    nome = data.get('nome')
    curso = data.get('curso')

    if not nome or not curso:
        return jsonify({"message": "Nome e curso são obrigatórios!"}), 400

    with open(csv_file, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([nome, curso])

    return jsonify({"message": "Cadastro realizado com sucesso!"}), 201

if __name__ == '__main__':
    app.run(debug=True)
