from flask import request, Flask, render_template
from app.models import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
db.init_app(app)


@app.before_first_request
def test_data():
    db.create_all()

    for i in range(10):
        db.session.add(Person(name='Person ' + str(i)))

    db.session.commit()


@app.route('/')
def index():
    return render_template('index.html', people=Person.query.all())