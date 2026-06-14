from flask import Flask, render_template, request, redirect, url_for, flash
import os
from database import init_db

app = Flask(__name__)
# Chave secreta para gestão de sessões e mensagens flash
app.config['SECRET_KEY'] = 'uma_chave_secreta_muito_segura_para_a_pap'

# Inicializar a base de dados
init_db()

@app.route('/')
def index():
    # Página inicial (Landing page)
    return render_template('index.html')

@app.route('/login/cliente', methods=['GET', 'POST'])
def login_cliente():
    if request.method == 'POST':
        # Simulação simples de login
        return redirect(url_for('dashboard_cliente'))
    return render_template('login_cliente.html')

@app.route('/login/helpdesk', methods=['GET', 'POST'])
def login_helpdesk():
    if request.method == 'POST':
        # Simulação simples de login
        return redirect(url_for('dashboard_helpdesk'))
    return render_template('login_helpdesk.html')

@app.route('/dashboard/cliente')
def dashboard_cliente():
    return render_template('dashboard_cliente.html')

@app.route('/dashboard/helpdesk')
def dashboard_helpdesk():
    return render_template('dashboard_helpdesk.html')

if __name__ == '__main__':
    # O debug=True permite que as alterações recarreguem o servidor automaticamente
    app.run(debug=True, port=5000)
