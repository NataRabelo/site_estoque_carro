from flask import Blueprint, render_template
from app.models import Car

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def landpage():
    carros = Car.query.all()
    return render_template('landpage.html', carros=carros)
