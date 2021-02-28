from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField, DateTimeField,
                     RadioField,SelectField,TextField,
                     TextAreaField,SubmitField, IntegerField)


class AddPetsForm(FlaskForm):
    name = StringField('Name of Pet:')
    submit = SubmitField('Add Pet')

class DeletePetsForm(FlaskForm):
    pet_id = IntegerField('Enter id number of pet to remove:')
    submit = SubmitField('Remove the pet')
