from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, URLField, TextAreaField, BooleanField
from wtforms.validators import DataRequired, URL, NumberRange, ValidationError


# Create pet form


class PetForm(FlaskForm):
    name = StringField('Name', render_kw={
                       'placeholder': 'Enter pet name...'}, validators=[DataRequired()])
    species = StringField('Specie', render_kw={
        'placeholder': 'Pet specie...'}, validators=[DataRequired()])
    photo_url = URLField('Photo Url', render_kw={
        'placeholder': 'Photo Url...'}, validators=[URL(require_tld=False)])
    age = IntegerField('Age', render_kw={
                       'placeholder': 'Enter pet age...'}, validators=[NumberRange(min=0, max=30)])
    notes = TextAreaField('Notes', render_kw={
        'placeholder': 'Notes about pet...'},)
    available = BooleanField('Available', render_kw={
        'placeholder': 'Available for adoption ( True/False )'}, validators=[DataRequired()])


class UserForm(FlaskForm):
    username = StringField('Username', render_kw={
                           'placeholder': 'Choose a unique username...'}, validators=[DataRequired()])

    first_name = StringField('First Name', render_kw={
                             'placeholder': 'Your First Name...'}, validators=[DataRequired()])

    last_name = StringField('Last Name', render_kw={
                            'placeholder': 'Enter Last Name...'})
