# User Story 3 (User Activities)

import os
from flask import Flask, render_template, url_for, redirect
from flask import request, session
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

db = SQLAlchemy(app)
Migrate(app, db)

class Comment(db.Model):
    
    __tablename__ = 'User Comments'
    id = database.Column(db.Integer, db.ForeignKey('owners'))
    pet_id = database.Column(db.Integer, db.ForeignKey('pets'))
    text = database.Column(db.String(200), primary_key = True)

# Insert comment function
@app.route('/comment', methods = ['GET', 'POST'])
def comment():

    if __name__ == '__main__':
        app.run()


@app.route('/like', methods = ['GET', 'POST'])
def share():

@app.route('/share', methods = ['GET', 'POST"])
def share():
