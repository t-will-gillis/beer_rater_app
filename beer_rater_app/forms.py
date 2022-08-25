from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField, SubmitField, FileField,\
        SelectField, SelectMultipleField, DecimalField, IntegerField, TextAreaField
from wtforms.widgets import ListWidget, CheckboxInput, RadioInput
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, NumberRange, Optional, NoneOf, InputRequired
from models import Beer, Brewery, User, Review




# Note that below only loads ONCE at beginning. We need to be dynamic!!!!!!!!!!!!!!!!!!!!
def brewery_choices():
    choices = [('8888','-Select Brewery-')]
    breweries = Brewery.query.order_by(Brewery.brewery_name).all()
    for brewery in breweries:
        choices.append((brewery.id, brewery.brewery_name))
    choices.append(('9999' ,'-Add Brewery-'))
    return choices







class SignupForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    city = StringField('City')
    state = StringField('State')
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Reenter Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

# class LoginForm(FlaskForm):



# Create BeerForm, use SelectField to select from existing list of breweries, use SelectMultipleField to select style
# note that there is a potential issue using SelectMultipleField- to avoid use request.form.getlist('...')??????
# Should it be FormField instead? 
# What about FileField for a photo?

class BeerForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    brewery_id = SelectField('Brewery', choices=brewery_choices(), validators=[InputRequired()], coerce=int)
    # style = SelectMultipleField('Style', validators=[DataRequired()])
    style = StringField('Style')
    abv = DecimalField('ABV', places=1, validators=[Optional(), NumberRange(min=0.5, max=50)])
    ibu = IntegerField('IBU', validators=[Optional()])
    num_reviews = IntegerField('NumReviews')
    
    submit = SubmitField('AddBeer')
    
class BreweryForm(FlaskForm):
    brewery_name = StringField('BreweryName', validators=[DataRequired()])
    brewery_city = StringField('BreweryCity', validators=[DataRequired()])
    brewery_state = StringField('BreweryState', validators=[DataRequired()])
    brewery_url = StringField('BreweryURL')
    submit = SubmitField('AddBrewery')

class ReviewForm(FlaskForm):
    overall = DecimalField('Overall', places=1, validators=[DataRequired()])
    look = DecimalField('Look', places=1)
    smell = DecimalField('Smell', places=1)
    taste = DecimalField('Taste', places=1)
    feel = DecimalField('Feel', places=1)
    notes = TextAreaField('ReviewNotes')
    submit = SubmitField('AddReview')
