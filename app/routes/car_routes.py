import os
from flask import Blueprint, render_template, request, redirect, url_for, flash, current_app
from werkzeug.utils import secure_filename
from app.models import Car
from app import db

car_bp = Blueprint('car', __name__)

UPLOAD_FOLDER = os.path.join(os.getcwd(),'app', 'static','images')
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    """Verifica se o arquivo tem uma extensão permitida."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@car_bp.route('/dashboard')
def dashboard():
    cars = Car.query.all()
    return render_template('dashboard.html', cars=cars)


@car_bp.route('/add_car', methods=['GET', 'POST'])
def add_car():
    if request.method == 'POST':
        # Obter os campos do formulário
        marca = request.form.get('marca')
        modelo = request.form.get('modelo')
        preco = request.form.get('preco')

        # Verificar se os campos obrigatórios foram preenchidos
        if not marca or not modelo or not preco:
            flash('Todos os campos são obrigatórios!')
            return redirect(request.url)

        # Verificar se o arquivo foi enviado
        if 'image' not in request.files:
            flash('Nenhuma imagem foi enviada!')
            return redirect(request.url)

        image = request.files['image']

        # Validar o arquivo
        if image.filename == '':
            flash('Nenhuma imagem selecionada!')
            return redirect(request.url)

        if not allowed_file(image.filename):
            flash('Formato de arquivo não permitido! Use PNG, JPG, JPEG ou GIF.')
            return redirect(request.url)

        # Salvar a imagem no diretório de uploads
        filename = secure_filename(image.filename)
        image_path = os.path.join(UPLOAD_FOLDER, filename)
        image.save(image_path)

        # Criar o novo carro e salvar no banco de dados
        new_car = Car(marca=marca, modelo=modelo, preco=preco, image_url=filename)
        db.session.add(new_car)
        db.session.commit()

        flash('Carro cadastrado com sucesso!')
        return redirect(url_for('car.dashboard'))

    return render_template('add_car.html')


@car_bp.route('/edit_car/<int:id>', methods=['GET', 'POST'])
def edit_car(id):
    car = Car.query.get(id)

    if request.method == 'POST':
        # Obter os dados do formulário
        car.marca = request.form['marca']
        car.modelo = request.form['modelo']
        car.preco = request.form['preco']

        # Verificar se uma nova imagem foi enviada
        if 'image' in request.files:
            image = request.files['image']
            if image.filename != '':
                if not allowed_file(image.filename):
                    flash('Formato de arquivo não permitido! Use PNG, JPG, JPEG ou GIF.')
                    return redirect(request.url)
                filename = secure_filename(image.filename)
                image_path = os.path.join(UPLOAD_FOLDER, filename)
                image.save(image_path)
                car.image_url = filename

        db.session.commit()
        flash('Carro atualizado com sucesso!')
        return redirect(url_for('car.dashboard'))

    return render_template('edit_car.html', car=car)


@car_bp.route('/delete_car/<int:id>', methods=['POST'])
def delete_car(id):
    car = Car.query.get(id)
    db.session.delete(car)
    db.session.commit()
    flash('Carro deletado com sucesso!')
    return redirect(url_for('car.dashboard'))
