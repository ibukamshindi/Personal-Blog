from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField
from wtforms.validators import Required,Email,EqualTo
from wtforms import ValidationError
from flask_wtf.file import FileAllowed,FileField
from flask_login import current_user
from app.models import User

class RegistrationForm(FlaskForm):
    email = StringField('Email',validators=[Required(),Email()])
    username = StringField('Username',validators=[Required()])
    password = PasswordField('Password', validators=[Required(), EqualTo('password_confirm',message='Password must match!')])
    password_confirm = PasswordField('Confirm Password', validators=[Required()])
    submit = SubmitField('Register')

    def validate_email(self,data_field):
        if User.query.filter_by(email=data_field.data).first():
            raise ValidationError('There is an account with that email')

    def validate_username(self, data_field):
         if User.query.filter_by(username=data_field.data).first():
            raise ValidationError('That username is taken')
class LoginForm(FlaskForm):
    email = StringField('Email',validators=[Required(),Email()],render_kw={"placeholder": "Email"})
    password = PasswordField('Password',validators=[Required()],render_kw={"placeholder": "Password"})
    remember = BooleanField('Remember me')
    submit = SubmitField('Log In')

class UpdateUserForm(FlaskForm):
    email = StringField('Email', validators=[Required(), Email()])
    username = StringField('Username', validators=[Required()])
    # picture = FileField('Update Profile Picture',validators=[FileAllowed(['jpg','png'])])
    submit = SubmitField('Update')

    def check_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Your email has been registered already!')

    def check_username(self, field):
         if User.query.filter_by(username=field.data).first():
            raise ValidationError('Your username has been registered already!')