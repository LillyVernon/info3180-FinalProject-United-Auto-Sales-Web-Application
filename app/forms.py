from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,validators,PasswordField,SelectField
from wtforms.validators import DataRequired, InputRequired
from flask_wtf.file import FileField, FileRequired, FileAllowed

class RegisterForm(FlaskForm):

    username=StringField('username', validators=[InputRequired()])
    fullname=StringField('fullname', validators=[InputRequired()])
    email = StringField('email', [validators.Length(min=6, max=35)])
    password = PasswordField('password', [validators.DataRequired()])
    location=StringField('location', validators=[InputRequired()])
    biography= TextAreaField('biography', validators=[InputRequired()])
    photo = FileField('Upload Photo', validators=[FileRequired(), FileAllowed(['jpg', 'png', 'Images only!'])])

class AddCarForm(FlaskForm):
    make=StringField('Make', validators=[InputRequired()])
    model=StringField('Model', validators=[InputRequired()])
    colour = StringField('Colour', validators=[InputRequired()])
    year = StringField('Year', validators=[InputRequired()])
    price = StringField('Price', validators=[InputRequired()])
    car_type=SelectField('Car Type',choices=[('SUV', 'SUV'), ('Lexus','Lexus'), ('Lamborghini','Lamborghini')])
    transmission=SelectField('Transmission',choices=[('Automatic', 'Automatic'), ('Manual','Manual')])
    description=TextAreaField('Description', validators=[InputRequired()])
    photo = FileField('Upload Photo', validators=[FileRequired(), FileAllowed(['jpg', 'png', 'Images only!'])])

class LoginForm(FlaskForm):
    username=StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', [validators.DataRequired()])
    
class Search(FlaskForm):
    make=StringField('Make')
    model=StringField('Model')


