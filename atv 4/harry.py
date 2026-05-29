from flask import Flask, render_template, abort

app = Flask(__name__)

# Banco de dados criativo dos destinos
DESTINOS = {
    'cyberpunk': {
        'nome': 'Neo-Tóquio 2077',
        'descricao': 'Luzes neon, chuva eterna e tecnologia de ponta.',
        'cor': '#ff0055'
    },
    'solarpunk': {
        'nome': 'Eco-Utopia',
        'descricao': 'Cidades verdes, energia solar e harmonia com a natureza.',
        'cor': '#2ecc71'
    },
    'medieval': {
        'nome': 'Reino de Eldoria',
        'descricao': 'Dragões, castelos e poções mágicas duvidosas.',
        'cor': '#f1c40f'
    },
    'vazio': {
        'nome': 'O Vazio Existencial',
        'descricao': 'Silêncio total. Ótimo para meditar ou questionar tudo.',
        'cor': '#2c3e50'
    }
}

@app.route('/')
def index():
    # Passamos apenas as chaves (tags) para a home
    return render_template('index.html', tags=DESTINOS.keys())

@app.route('/viajar/<tag>')
def viajar(tag):
    dados = DESTINOS.get(tag)
    if not dados:
        abort(404)
    return render_template('destino.html', destino=dados)

if __name__ == '__main__':
    app.run(debug=True)