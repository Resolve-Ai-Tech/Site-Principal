from flask import Flask, render_template
from flask_session import Session

app = Flask(__name__, template_folder="../frontend/templates")

app.static_folder = '../frontend/src'
app.static_url_path = '/static'

app.config['SECRET_KEY'] = 'supersecretkey'
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

@app.route('/')
def index():
    projeto = [{'nome': 'Melodia', 'tipo': 'Aplicativo de Música', 'versao': 'BETA', 'descricao': 'fansadkdsandaspdas'}]
    
    return render_template('index.html', projetos=projeto)

@app.route('/logar')
def logar():
    pass

@app.route('/login')
def login():
    pass

@app.route('/registro')
def registro():
    pass

@app.route('/dashboard')
def dashboard():
    pass
    
if __name__ == '__main__':    
    app.run(debug=True, port=8000)