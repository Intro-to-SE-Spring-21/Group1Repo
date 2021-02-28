import os
from PetBookforms import  AddPetsForm , DeletePetsForm
from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

# Key for Forms
app.config['SECRET_KEY'] = 'secret_key_here'


        # SQLite DATABASE

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

database = SQLAlchemy(app) #Create database by passing our application to database
Migrate(app,database) # Setting up migration for database updates

class Pets(database.Model):

    __tablename__ = 'pets'
    pet_id = database.Column(database.Integer,primary_key = True)
    name = database.Column(database.Text)


    def __init__(self,name):
        self.name = name

    def __repr__(self):
        return "The name of the pet is {}".format(self.name)


@app.route('/')
def index():
    return render_template('home.html')

@app.route('/add', methods=['GET', 'POST'])
def add_pet():
    form = AddPetsForm()

    if form.validate_on_submit():
        name = form.name.data

        # Add new Pets to database
        new_pets = Pets(name)
        database.session.add(new_pets)
        database.session.commit()

        return redirect(url_for('list_pet'))

    return render_template('add_pets.html',form=form)

@app.route('/list')
def list_pet():
    # Grab a list of pets from database.
    pets = Pets.query.all()
    return render_template('list_pets.html', pets=pets)

@app.route('/delete', methods=['GET', 'POST'])
def del_pet():
    form = DeletePetsForm()

    if form.validate_on_submit():
        pet_id = form.pet_id.data
        pet = Pets.query.get(pet_id)
        database.session.delete(pet)
        database.session.commit()

        return redirect(url_for('list_pet'))
    return render_template('delete_pets.html',form=form)


if __name__ == '__main__':
    app.run(debug=True)
