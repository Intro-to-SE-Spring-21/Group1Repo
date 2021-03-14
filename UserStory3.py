# User Story 3 (User Activities)
# Edited by Patrick Asher and Matthew Gentry

import os
from flask import Flask, render_template, url_for, redirect, request, session
from flask_login import login_required
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf import FlaskForm
from wtforms import TextAreaField
from wtforms.validators import InputRequired
from flask_wtf.file import FileField, FileAllowed

app = Flask(__name__)

db = SQLAlchemy(app)
Migrate(app, db)

# a class for posts
class Post(db.Model):
    #like and number of likes may not need to be primary keys?

    #gets the owner and pet of the post
    #possibly need picture or string of text as well?
    owner_id = database.Column(db.Integer, db.ForeignKey('owners.id'))
    pet_id = database.Column(db.Integer, db.ForeignKey('pets.pet_id'))

    #creates a boolean variable for if the post was liked
    like = database.Column(db.Boolean, primary_key = True)

    #creates an integer for the ammount of current likes on the post
    #may not be a correct declaration
    num_likes = database.Column(db.Integer, primary_key = True)

    #function to get the current flag/boolean like value of the post
    def getLike(self):
        return like

    # function to set the like value of a post
    def setLike(self, like):
        self.like = like

    #function to add a like to the number of likes
    def addLike(self):
        self.num_likes = num_likes + 1

    #function to subtract a like from the number of likes
    def subtractLike(self):
        self.num_likes = num_likes - 1

    #function to return the current number of likes back to the database/webpage
    def displayLikes(self):
        return num_likes

# class for comments
class Comment(db.Model):
    __tablename__ = 'User Comments'
    ident = database.Column(db.Integer, primary_key = True)
    owner_id = database.Column(db.Integer, db.ForeignKey('owners.id'))
    pet_id = database.Column(db.Integer, db.ForeignKey('pets.pet_id'))
    text = database.Column(db.Text), primary_key = True)

    # accepts text from a form
    def __init__(self, text):
        self.text = text

# Form for comments
class CommentForm(FlaskForm):
    text = TextAreaField('Add a comment...', validators=[InputRequired('Message is Required.')])

#function to like a post
@app.route('/like', methods = ['GET', 'POST'])
def like(self):

    #gets the current like value of the user from the post
    current_like = Post.getLike()

    #if the user has not liked the post, the function likes it and adds 1 to the number of likes
    if current_like == False:
        Post.setLike(True)
        Post.addLike()

    #if the user has already liked the post, the function unlikes it and subtracts one from the number of likes
    if current_like == True:
        Post.setLike(False)
        Post.subtractLike()     
    
    #the function then displays the current number of likes
    Post.displayLikes()

# Insert comment function
@app.route('/addComment', methods = ['GET', 'POST'])
@login_required
def addComment():
    if request.method == 'POST':
        form = CommentForm()

        # Check for comment input
        if form.validate_on_submit():
            comment = form.text.data

            # Add comment to the database
            new_comment = Comment(comment)
            database.session.add(new_comment)
            database.session.commit()

            return redirect(url_for('list_pets'))

        return 'Error!'
