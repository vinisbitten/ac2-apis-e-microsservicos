from flask import Flask, jsonify

app = Flask(__name__)

# Define a rota para a consulta GET
@app.route('/api/book', methods=['GET'])

def get_book():
    # Cria um dicionário com as informações do livro
    book = {
        'title': 'Harry Potter and the Philosopher\'s Stone',
        'author': 'J.K. Rowling',
        'published_year': 1997
    }

    # Retorna as informações do livro como JSON
    return jsonify(book), 200

if __name__ == '__main__':
    app.run()