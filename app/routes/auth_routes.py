from flask import Blueprint, render_template, request, redirect, url_for

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['usuario']
        password = request.form['senha']

        if username == 'admin' and password == '12345':
            return redirect(url_for('car.dashboard'))
        else:
            return "Usuário ou senha inválidos", 401

    return render_template('login.html')
