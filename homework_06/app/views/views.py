from datetime import datetime
from flask import render_template, Blueprint, request, redirect, url_for

pages = Blueprint('page', __name__)

@pages.route('/')
def index():
    return render_template('index.html')

@pages.route('/create/')
def create_product():
    return render_template('create.html')

@pages.route('/add/', methods=['POST'])
def add_product(): 
    from models.db_models import EducationProductModel
    from main import app
    ep_name_ = request.form.get("ep_name")
    ep_duration_ = request.form.get("ep_duration")
    ep_price_ = request.form.get("ep_price")
    new_product = EducationProductModel(ep_name_, ep_duration_, ep_price_)

    with app.app_context():
        from main import db
        db.session.add(new_product)
        db.session.commit()

    return render_template('index.html')

@pages.route('/list')
def get_list():
    from models.db_models import EducationProductModel
    from main import app
    with app.app_context():
        produsts = EducationProductModel.query.all()
        data = []
        for p in produsts:
            print(p.ep_name)
            data.append({"id": p.id, "name": p.ep_name, "duration": (f'{p.ep_duration} ак.ч.') , "price": (f'{p.ep_price} руб.'), "date": datetime.strftime(p.ep_createDate, '%d.%m.%Y')})

    return render_template('list.html', data=data)