import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///cars.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY', 'secret')

    UPLOAD_FOLDER = os.path.join(os.getcwd(), 'app', 'static', 'images')
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)


    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
