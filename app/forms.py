from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField
from wtforms.validators import DataRequired,Email,EqualTo,ValidationError
from app.models import User,Post

class LoginForm(FlaskForm):
    username = StringField('Username: ',validators=[DataRequired()])
    password = PasswordField('Password: ',validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Log in')

class RegisterForm(FlaskForm):
    username = StringField('username: ',validators=[DataRequired()])
    email = StringField('email: ',validators=[DataRequired(),Email()])
    password = PasswordField('password: ',validators=[DataRequired()])
    password2 = PasswordField('comfirm password: ',validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField('Register')
    def validate_username(self,username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use different username !!')
    def validate_email(self,email):
        email = User.query.filter_by(email=email.data).first()
        if email is not None:
            raise ValidationError('Please use different email !!')
            