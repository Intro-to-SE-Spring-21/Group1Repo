from flask import render_template, redirect, request, url_for, flash,abort
from flask_login import login_user,login_required,logout_user
from myproject.models import User
from myproject.forms import LoginForm
from werkzeug.security import generate_password_hash, check_password_hash 
from flask_bcrypt import Bcrypt


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/welcome')
@login_required
def welcome_PetBook_User():
    return render_template('Welcome_PetBook_user.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have logged out off PetBook!')
    return redirect(url_for('home'))


@app.route('/login', methods=['GET', 'POST'])
def login():
