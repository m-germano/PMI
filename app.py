from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    itens=['Home', 'Quem Somos', 'Contato']
    return render_template('index.html', itens=itens)

@app.route('/contato')
def contato():
    return render_template('contato.html')

@app.route('/quemsomos')
def quemsomos():
    itens_aula=['Material sempre atualizado', 'Tablets em sala de aula','Professores renomados','Universidade bem avaliada','Otima localização']
    return render_template('quemsomos.html', itens=itens_aula)

if __name__ == "__main__":
    app.run(debug=True)