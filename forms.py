from wtforms import Form, StringField, PasswordField, SelectField,\
                    BooleanField, validators

class LoginForm(Form):
    username = StringField('username', [validators.DataRequired()])
    password = PasswordField('password', [validators.DataRequired()])

class RegistrationForm(Form):
    username = StringField('username', [validators.DataRequired()])
    first_name = StringField('first_name', [validators.DataRequired()])
    last_name = StringField('last_name', [validators.DataRequired()])
    password = PasswordField('password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('confirm')
